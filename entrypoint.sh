#!/bin/sh
set -e

echo "⏳ Waiting for Postgres..."

# Wait for DB to be ready
until nc -z "$DATABASE_HOST" 5432; do
  echo "Waiting for database..."
  sleep 1
done

echo "✅ Postgres is up"

echo "📦 Running migrations..."
python manage.py migrate --noinput --verbosity 2 || echo "Migrations already applied"

echo "⚙️ Loading default settings..."
python load_settings.py || echo "Default settings already loaded"

echo "👤 Creating admin..."
python manage.py shell < superuser.py || echo "Admin already exists"

echo "🚀 Starting server"
# exec python manage.py runserver 0.0.0.0:8000 #dev server
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --threads 4 gabm_infra.wsgi:application #prod server
