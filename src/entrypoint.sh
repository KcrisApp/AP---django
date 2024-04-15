#!/bin/ash

echo "Apply database migrations"

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


# Svuoto il DB
# python manage.py flush --no-input

# Migrate
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py initadmin

# collect statics file
python manage.py collectstatic --no-input   


exec "$@"