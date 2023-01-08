#Description: install Docker and Docke-compose on AmazonLinux

#!/bin/bash

#install Docker
sudo yum update
sudo yum install docker -y

#Enable docker service at boot time
sudo systemctl enable docker.service
#Start the Docker
sudo systemctl start docker.service

#Check Docker version and status
echo "***************Docker status***************"
sudo systemctl status docker.service
echo "***************Docker version***************"
docker --version

#Add group membership for the default user so you can run all docker commands without using the sudo command
sudo usermod -aG docker $USER
newgrp docker

#Install Docker compose
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version