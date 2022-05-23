#!/bin/sh
if [ "$WAITFORDATABASE" = 'true' ]; then
  echo "Waiting for database..."

  while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
    sleep 0.1
  done

  echo "database started"
fi

exec "$@"
