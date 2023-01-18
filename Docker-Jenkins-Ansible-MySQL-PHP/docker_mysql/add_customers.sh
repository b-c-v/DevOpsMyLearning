#Description: add information to DB

#!/usr/bin/env bash
set -euxo pipefail #stop working of script if be error

mysql -u root -h mysql_docker -p1234 -e "CREATE DATABASE people;
   USE people;
   CREATE TABLE customers (
     PersonID int,
     FirstName varchar(255),
     LastName varchar(255),
     Age int (3)
  );
  "

count=0

while [[ $count -lt 50 ]]; do
  let "count=count+1"

  first_name=$(nl customers.txt | grep -w $count | awk '{print $2}' | awk -F ',' '{print $1}')

  last_name=$(nl customers.txt | grep -w $count | awk '{print $2}' | awk -F ',' '{print $2}')

  age=$(shuf -i 20-25 -n 1) #shuf - generate random numbers from 20 to 25 and return first number (-n 1)

  mysql -u root -h mysql_docker -p1234 people -e "INSERT INTO customers (PersonID, FirstName, LastName, Age) VALUES ($count,'$first_name', '$last_name', $age);" #add data to table customer

done
