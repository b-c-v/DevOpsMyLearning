#Description: make backup of DB and copy it to S3 bucket

#!/bin/bash

DATE=$(date +%H-%M-%S)  #data in format hours-minutes-seconds
BACKUP=db-$DATE.sql     #add date to name of backup file

DB_HOST=$1
DB_PASSWORD=$2
DB_NAME=$3

AWS_ID=$4
AWS_KEY=$5

BUCKET_NAME=$6

mysqldump -u root -h $DB_HOST --password="$DB_PASSWORD" $DB_NAME > /tmp/$BACKUP && \
export AWS_ACCESS_KEY_ID=$AWS_ID && \
export AWS_SECRET_ACCESS_KEY=$AWS_KEY && \
echo "Uploading your $BACKUP backup" && \
aws s3 cp /tmp/db-$DATE.sql s3://$BUCKET_NAME/$BACKUP