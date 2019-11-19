#!/bin/bash
source ../flask/bin/activate
#gunicorn -w 1 -k gevent --bind=0.0.0.0:6969 app:app
#gunicorn -w 1 --bind=127.0.0.1:6969 app:app
gunicorn -w 1 --bind=0.0.0.0:6969 app:app
