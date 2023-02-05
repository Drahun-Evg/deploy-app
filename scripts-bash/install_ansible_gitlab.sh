#!/bin/bash

#1) Ansible
echo --------- Starting Install Ansible ---------
PATH_ANSIBLE=/etc/ansible #Путь где будут распологаться ваши конфигфайлы

sudo apt update
sudo apt install ansible -y
sudo mkdir "$PATH_ANSIBLE" #Создание папки для описания конфигфайлов
sudo touch "$PATH_ANSIBLE"/hosts #Создание файлов для описания хостов
sudo touch "$PATH_ANSIBLE"/ansible.cfg
sudo chmod 666 "$PATH_ANSIBLE"/ansible.cfg
sudo cat << EOF > "$PATH_ANSIBLE"/ansible.cfg
[defaults]
inventory = "$PATH_ANSIBLE"/hosts
host_key_checking = false
interpreter_python = /usr/bin/python3
EOF
ansible --version
echo ---------- Finish installing Ansible ----------

#2) Git
echo --------- Starting Install Git ---------
sudo apt update
sudo apt install -y git
git --version
echo --------- Finist Install Git ---------


#3) GitLab
YOUR_URL=http://gitlab-server.local

echo --------- Starting Install Gitlab ---------
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates perl
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
sudo EXTERNAL_URL="$YOUR_URL" apt-get install gitlab-ce
echo  ---------- Finish installing GitLab ----------
