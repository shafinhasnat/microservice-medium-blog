#!/bin/bash

echo "waiting.."
while ! nc -z 1.2.3.4 5432; do
    sleep 0.1
done
echo "postgres connection established"

gunicorn -w 4 --bind 0.0.0.0:5000 manage:app