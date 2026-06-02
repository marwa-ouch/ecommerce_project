#!/bin/sh

echo "Application Django : démarrage..."

echo "Application des migrations..."
python manage.py migrate --noinput

echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "Lancement du serveur..."
exec "$@"