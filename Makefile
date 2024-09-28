ins:
	pip install $(name)
	# exam -> make ins name=django

req:
	pip freeze > requirement.txt
     #exam -> make req
app:
	python3 manage.py startapp $(name)
    # exam -> make app name=account
