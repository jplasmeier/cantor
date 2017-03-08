# Cantor 

An API for client/server communication between a Geospatial Database and a Map UI.

Cantor loosely follows RESTful and HATEOAS design principles. 

## Installation

You will need to have `pyvenv-3.5` installed. 

* Clone this repository, `cd` into it.
* Create a Python3 virtualenv: `python3 -m venv ./env`
* Activate the virtual environment: `source env/bin/activate`
* Install requirements with pip: `pip install -r requirements.txt`
* Make migrations: `python manage.py makemigrations`
* Run migrations: `python manage.py migrate`
* Run the server: `python manage.py runserver`

