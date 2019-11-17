#!/bin/bash
cd home-service
gunicorn -w 2 --bind=0.0.0.0:8777 app:app
