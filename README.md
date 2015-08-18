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

- env
  + export STEPBYSTEP_DB='stepbystep'
  + export STEPBYSTEP_CONFIG='production'
  + export STEPBYSTEP_LOG_LEVEL='ERROR'

- cli 
  + python manage.py deploy
  + celery -A stepbystep.libs.tasks:celery worker -B --logfile=celery.log &
  + gunicorn -w 4 manage:app --log-file gunicorn.log -b 0.0.0.0:4000 &

## Stop 

### stoping celery worker

- ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
