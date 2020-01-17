#!/bin/bash
source flask/bin/activate
gunicorn -w 1 --bind=0.0.0.0:6969 "home_service:create_app()"
