release: python manage.py migrate --no-input
web: waitress-serve --port=$PORT icmo.wsgi:application
worker: python manage.py rqworker default & python manage.py rqworker default & python manage.py rqworker integrations & python manage.py rqworker integrations
scheduler: python manage.py rqscheduler default