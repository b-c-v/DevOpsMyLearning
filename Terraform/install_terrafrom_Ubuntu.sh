#!/bin/bash

#install terraform
curl https://releases.hashicorp.com/terraform/1.3.6/terraform_1.3.6_linux_amd64.zip -o terraform.zip
unzip terraform.zip
sudo mv terraform /bin/
rm terraform.zip