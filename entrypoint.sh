#!/bin/sh
if [ "$WAIT_FOR_DB" = 1 ]; then
  echo "Waiting for database..."

  while ! nc -z "$DB_HOST" "$DB_PORT"; do
    sleep 0.1
  done

  echo "database started"
fi

exec "$@"
