#!/bin/bash
source flask/bin/activate
gunicorn -w 2 -k gevent --bind=0.0.0.0:6969 app:app
