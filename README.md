# Application E-Commerce Django

> Application web e-commerce développée avec le framework Django dans le cadre du cours Développement Web Python 2026.

---

## Table des Matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Structure du Projet](#structure-du-projet)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Configuration de la Base de Données](#configuration-de-la-base-de-données)
- [URLs de l'Application](#urls-de-lapplication)
- [Modèles de Données](#modèles-de-données)


---

## Aperçu

Ce projet constitue une application web e-commerce complète, réalisée avec le framework **Django** et suivant l'architecture **MVT (Modèle-Vue-Template)**. 

Les concepts abordés incluent :

- La modélisation des données avec l'ORM Django
- La gestion des migrations de base de données
- La création de vues basées sur des fonctions
- L'héritage de templates HTML
- La personnalisation de l'interface d'administration
- L'intégration d'une base de données MySQL via Docker

---

## Fonctionnalités

- **Liste des produits** — Affichage de l'ensemble des produits avec leurs images, prix et catégories associées
- **Détail d'un produit** — Consultation des informations complètes d'un produit (description, stock, catégorie, image)
- **Liste des catégories** — Navigation parmi toutes les catégories disponibles
- **Détail d'une catégorie** — Affichage de tous les produits appartenant à une catégorie donnée
- **Upload d'images** — Gestion des images produits via le champ `ImageField` de Django (bibliothèque Pillow)
- **Interface d'administration** — Gestion CRUD complète des produits et catégories via le panneau d'administration Django
- **Base de données MySQL** — Persistance des données sur un serveur MySQL conteneurisé avec Docker

---

## Structure du Projet
```

ecommerce_project/
├── ecommerce/                    # Répertoire principal du projet Django
│   ├── settings.py               # Fichier de configuration du projet
│   ├── urls.py                   # Configuration des URLs racine
│   ├── wsgi.py
│   └── asgi.py
│
├── products/                     # Application Django "products"
│   ├── migrations/               # Fichiers de migration de la base de données
│   ├── templates/                # Templates HTML de l'application
│   │   ├── layout.html           # Template de base (avec Bootstrap 5)
│   │   ├── product_list.html     # Affichage de la liste des produits
│   │   ├── product_detail.html   # Affichage du détail d'un produit
│   │   ├── category_list.html    # Affichage de la liste des catégories
│   │   └── category_detail.html  # Affichage du détail d'une catégorie
│   ├── models.py                 # Définition des modèles Category et Product
│   ├── views.py                  # Fonctions de vues
│   ├── urls.py                   # Configuration des URLs de l'application
│   ├── admin.py                  # Configuration de l'espace d'administration
│   └── apps.py
│
├── images/                       # Répertoire de stockage des fichiers médias
│   └── products/                 # Images des produits uploadées
│
├── docker-compose.yaml           # Configuration du conteneur MySQL
└── manage.py                     # Point d'entrée des commandes Django
```

---

## Technologies Utilisées

| Technologie | Rôle |
|---|---|
| Python 3.x | Langage de programmation principal |
| Django | Framework web (architecture MVT) |
| MySQL | Système de gestion de base de données |
| Docker | Conteneurisation de la base de données |
| Bootstrap 5 | Framework CSS pour l'interface utilisateur |
| Pillow | Traitement et gestion des images |
| mysqlclient | Connecteur Python-MySQL compatible Django |

---

## Installation

### Prérequis

- Python 3.x installé sur la machine
- Docker et Docker Compose installés
- pip (gestionnaire de paquets Python)

### Étape 1 — Cloner le dépôt


```bash
git clone https://github.com/marwa-ouch/ecommerce_project.git
cd ecommerce_project
```

### Étape 2 — Créer et activer l'environnement virtuel

```bash
pip install virtualenv
python3 -m venv django_env
source django_env/bin/activate
```

### Étape 3 — Installer les dépendances

```bash
pip install django
pip install pillow
pip install mysqlclient
```

### Étape 4 — Démarrer la base de données MySQL via Docker

```bash
docker-compose up -d
```

### Étape 5 — Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Étape 6 — Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### Étape 7 — Lancer le serveur de développement

```bash
python manage.py runserver
```

---

## Configuration de la Base de Données

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_ecommerce',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
```

---

## URLs de l'Application

| URL | Vue associée | Description |
|---|---|---|
| `/products/` | `product_list` | Liste de tous les produits |
| `/products/<id>/` | `product_detail` | Détail d'un produit |
| `/products/categories/` | `category_list` | Liste de toutes les catégories |
| `/products/categories/<id>/` | `category_detail` | Détail d'une catégorie |
| `/admin/` | Interface Admin | Panneau d'administration Django |

---

## Modèles de Données

### Modèle `Category`

| Champ | Type | Description |
|---|---|---|
| `name` | `CharField(max_length=100)` | Nom unique de la catégorie |
| `description` | `TextField` | Description optionnelle |
| `created_at` | `DateTimeField(auto_now_add=True)` | Date de création automatique |

### Modèle `Product`

| Champ | Type | Description |
|---|---|---|
| `name` | `CharField(max_length=255)` | Nom du produit |
| `description` | `TextField` | Description détaillée |
| `price` | `DecimalField(max_digits=10, decimal_places=2)` | Prix du produit |
| `stock` | `IntegerField` | Quantité disponible en stock |
| `category` | `ForeignKey(Category)` | Référence à la catégorie (relation N-1) |
| `image` | `ImageField` | Image du produit (optionnelle) |
| `created_at` | `DateTimeField(auto_now_add=True)` | Date de création automatique |

---

