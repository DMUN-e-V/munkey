# munkey
## Introduction
munkey can be used to manage MUN conferences. It is based on Django and wagtail.

## Development
To set up a development version of munkey on your local machine, you need to execute the following steps:
1. Set up Python >3.6 and a virtualenv for the project
2. Install poetry (if not already installed): `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
3. Check out repository and cd to it
4. Install dependencies with `poetry install`
5. Migrate the database with `python manage.py migrate`
6. Create a superuser with `python manage.py createsuperuser`
7. Start the development server with `python manage.py runserver`

Before commiting, make sure to lint your changes with `black .` or [IDE integration](https://github.com/psf/black#editor-integration) and to test the code with `python manage.py test`
