#!/bin/bash

#A. Create a script that uses the following keys:
#1. When starting without parameters, it will display a list of possible keys and their description.
#2. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet
#3. The --target key displays a list of open system TCP ports.
#The code that performs the functionality of each of the subtasks must be placed in a separate function

command -v netstat  >/dev/null 2>&1 || { echo >&2 "For working this script please install netstat.  Aborting."; exit 1; }
command -v awk  >/dev/null 2>&1 || { echo >&2 "For working this script please install awk.  Aborting."; exit 1; }

all_function () {
  sub=$(ip -o -f inet addr show | awk '/scope global/ {print $4}')
  nmap -sP $sub | awk '/Nmap scan report/{print}' | sed 's/Nmap scan report for//'
}

target_function () {
netstat -ant | awk '/LISTEN/ { print $4 }' | rev | cut -f1 -d: | rev
}

case $1 in
"--all")
all_function
;;
"--target")
target_function
;;
"") 
echo "Please input key:
--all - key displays the IP addresses and symbolic names of all hosts in the current subnet
--target - key displays a list of open system TCP ports."
;;
* ) echo "wrong parameter"
esac


