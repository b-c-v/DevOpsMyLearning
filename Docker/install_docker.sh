#!/bin/bash
sudo apt-get update
sudo apt-get install curl -y
sudo apt-get remove docker docker-engine docker.io containerd runc -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh -y
sudo usermod -aG docker $USER
newgrp docker