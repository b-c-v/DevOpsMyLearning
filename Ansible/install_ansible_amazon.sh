#!/bin/bash

sudo amazon-linux-extras enable python3.8 -y
sudo pip3 install ansible -y
ansible --version
