#!/bin/bash

DB_NAME=support
DB_PASS=root
DB_USER=root

#1) Install Postgresql

#sudo yum update -y
sudo subscription-manager register --auto-attach
sudo yum info postgresql-server
sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo yum repolist -y
sudo yum install git -y
#sudo yum -y update

sudo yum install -y postgresql14-server postgresql14
sudo rpm -qi postgresql14-server postgresql14
sudo /usr/pgsql-14/bin/postgresql-14-setup initdb
sudo systemctl enable --now postgresql-14
sudo systemctl status postgresql-14
echo "Done install database!"

#2) Create DB and user for app

sudo -u postgres createuser -s -i -d -r -l -w root
sudo -u postgres psql -c "ALTER ROLE $DB_USER WITH PASSWORD '$DB_PASS'"
sudo service postgresql restart
echo "Done create user!"

sudo -u postgres psql -c "CREATE DATABASE $DB_NAME"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER"
echo "Done create DB!"

#3) Install python3 and pip

sudo yum -y install epel-release
sudo yum -y update
sudo yum -y groupinstall "Development Tools"
sudo yum -y install openssl-devel bzip2-devel libffi-devel xz-devel
sudo yum -y install wget
wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz

tar xvf Python-3.8.12.tgz
cd Python-3.8*/
./configure --enable-optimizations

sudo make altinstall

python3.8 --version
pip3.8 --version
echo "Done install Python and pip!"
