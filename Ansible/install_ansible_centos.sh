#!/bin/bash

# https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html#installing-ansible-on-fedora-or-centos

sudo yum install epel-release -y
sudo yum install ansible -y
ansible --version
