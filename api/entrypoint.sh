#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "database" $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "Initializing the database"
flask db init
flask db migrate
echo "Database initialized"

uwsgi --ini /api/app.ini

exec "$@"
