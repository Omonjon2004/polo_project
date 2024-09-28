sort:
	black .
	isort .
ins:
	pip install $(name)
	# exam -> make ins name=django

req:
	pip freeze > requirements/base.txt
     #exam -> make req
app:
	python3 manage.py startapp $(name)
    # exam -> make app name=account
mig:
	python manage.py makemigrations
	python manage.py migrate

