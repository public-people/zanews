web: gunicorn --worker-class gevent zanews.wsgi:application --log-file -
release: python manage.py collectstatic