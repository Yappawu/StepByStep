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
- export STEPBYSTEP_LOG_LEVEL='ERROR'
- python manage.py deploy
- celery -A stepbystep.libs.tasks:celery worker --logfile=celery_work.log &
- celery -A stepbystep.libs.tasks:celery beat --logfile=celery_beat.log &
- gunicorn -w 4 manage:app --log-file gunicorn_error.log -b 0.0.0.0:4000 &

## Stop 

### stoping celery worker

- ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
