#!/bin/bash
cd /opt/
sudo wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.27/bin/apache-tomcat-10.0.27.tar.gz
sudo tar -xzf apache-tomcat-10.0.27.tar.gz && sudo mv apache-tomcat-10.0.27 tomcat
sudo rm apache-tomcat-10.0.27.tar.gz
