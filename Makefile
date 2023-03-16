free_port:
	netstat -aon | findstr :8000
	taskkill /PID [PID] /F

start:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

migrations:
	python manage.py showmigrations

shell:
	python manage.py shell

test:
	python manage.py test restaurant.tests

admin:
	python manage.py createsuperuser


db:
	python manage.py dbshell