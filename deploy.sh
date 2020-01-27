#!/bin/bash
source ./venv/bin/activate
gunicorn -w 2 --bind=0.0.0.0:6969 "home_service:create_app()"
