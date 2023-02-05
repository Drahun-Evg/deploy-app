#!/bin/bash

echo "Begin run app"

F_NAME=python-app
REP="$HOME"/"$F_NAME"

sudo apt install python3.8-venv
python3.8 -m venv "$REP"/env
source "$REP"/env/bin/activate
pip install -r "$REP"/requirements.txt
python3.8 "$REP"/manage.py makemigrations
python3.8 "$REP"/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'admin@example.com', 'root')" | python3.8 "$REP"/manage.py shell
python3.8 "$REP"/manage.py runserver

echo "Done!
