# StepByStep
SDUT StepByStep

## Installation

- pip install -r requirements.txt
- python manage.py deploy

## Usage

- python manage.py runserver
- redis-server
- celery -A VJ.libs.tasks:celery worker -B -l debug

## Import User Problem Category

- cd stepbystep/scripts
- python import_category_problem.py
- python import_user.py
