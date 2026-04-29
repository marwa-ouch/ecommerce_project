from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path(
    'password_reset/',
    auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'
    ),
    name='password_reset'
)
]