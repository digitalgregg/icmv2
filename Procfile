web: waitress-serve --port=$PORT icmo.wsgi:application
release:  python manage.py migrate && python manage.py collectstatic --noinput
worker: python manage.py rqworker default & python manage.py rqworker default & python manage.py rqworker integrations & python manage.py rqworker integrations
scheduler: python manage.py rqscheduler default