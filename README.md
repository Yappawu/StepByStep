# StepByStep
SDUT StepByStep

## Installation

- pip install -r requirements.txt
- python manage.py deploy

## Usage

- python manage.py runserver
- redis-server
- celery -A stepbystep.libs.tasks:celery worker -B -l debug

## Import User Problem Category

- cd stepbystep/scripts
- python import_category_problem.py
- python import_user.py

## Deploy

- export STEPBYSTEP_DB='stepbystep'
- export STEPBYSTEP_CONFIG='production'
- export LOG_LEVEL='ERROR'
- python manage.py deploy
- celery -A stepbystep.libs.tasks:celery worker -B --loglevel=ERROR --logfile=celery.log &
- gunicorn -w 4 manage:app --log-file=stepbystep.log --error-logfile stepbystep_error.log -b 0.0.0.0:4000 &

## Stop 

### stoping celery worker

- ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
