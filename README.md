![Workflow](https://github.com/DMUN-e-V/munkey/workflows/munkey/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/DMUN-e-V/munkey/badge.svg?branch=master)](https://coveralls.io/github/DMUN-e-V/munkey?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# munkey
## Introduction
munkey can be used to manage MUN conferences. It is based on Django and wagtail.

## Development
To set up a development version of munkey on your local machine, you need to execute the following steps:
1. Set up Python >3.6 and a virtualenv for the project
2. Install poetry (if not already installed): `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`
3. Check out repository and cd to it
4. Install dependencies with `poetry install`
5. Create env file with `cp .env.example .env`
6. Migrate the database with `python manage.py migrate`
7. Create a superuser with `python manage.py createsuperuser`
8. Start the development server with `python manage.py runserver`

Before commiting, make sure to lint your changes with `black .` or [IDE integration](https://github.com/psf/black#editor-integration) and to test the code with `python manage.py test`

When encoutering errors while running `python manage.py migrate`, you might need to delete the database (for sqlite simply delete the db.sqlite3 file). You might also need to install mysql, e.g. on macOS with `brew install mysql`
It might also be worthwile to checkout the wiki under Deployment!
