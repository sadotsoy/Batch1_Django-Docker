python manage.py migrate personas zero
python manage.py migrate lugares zero
python manage.py migrate users zero

python manage.py makemigrations
python manage.py migrate
gunicorn --bind 0.0.0.0:$PORT damnificados.wsgi:application
