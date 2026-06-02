from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem
from products.models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.select_related('product')

    total = sum(item.total_price() for item in items)

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
        'items': items,
        'total': total
    })

@login_required
def decrease_quantity(request, product_id):
    cart = Cart.objects.get(user=request.user)

    item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart_detail')

@login_required
def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)

    CartItem.objects.filter(cart=cart, product_id=product_id).delete()

    return redirect('cart_detail')

