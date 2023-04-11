#Description: Install Postgresql on Centos

#!/bin/bash

sudo yum install postgresql-server -y
# Initialize the Database
sudo postgresql-setup initdb
# Start the Database
sudo systemctl start postgresql.service
# Configure PostgreSQL to start on every system reboot automatically
sudo systemctl enable postgresql.service
