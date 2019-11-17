#!/bin/bash
source flask/bin/activate
cd home-service
gunicorn -w 2 -k gevent --bind=0.0.0.0:6969 app:app
