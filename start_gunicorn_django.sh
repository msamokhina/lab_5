#!/bin/bash
gunicorn -c gunicorn.conf.py Favorite.wsgi:application