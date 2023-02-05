#!/bin/bash

DB_NAME=support
DB_PASS=root
DB_USER=root

#1) Install git

echo "Start install GIT POSTGRESQL PYTHON  PIP"

sudo apt-get update
sudo apt-get install git -y
git --version
git clone https://github.com/Drahun-Evg/Build-Deploy-PythonApp.git
echo "Done Git!"

#2) Install Postgresql and create user

sudo apt-get install -y postgresql postgresql-client postgresql-contrib
sudo -u postgres createuser -s -i -d -r -l -w root
sudo -u postgres psql -c "ALTER ROLE $DB_USER WITH PASSWORD '$DB_PASS'"
sudo service postgresql restart

sudo -u postgres psql -c "CREATE DATABASE $DB_NAME"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER"
echo "Done DB!"

#3) Install Pip and python env plugin

sudo apt update
sudo apt install python3-pip -y
sudo apt install python3.8-venv

pip3 --version
echo "Pip Done!"
