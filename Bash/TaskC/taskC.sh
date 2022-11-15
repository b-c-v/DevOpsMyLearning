#!/bin/bash
# C. Create a data backup script that takes the following data as parameters:
# 1. Path to the syncing directory ($1).
# 2. The path to the directory where the copies of the files will be stored ($2)
# In case of adding new or deleting old files, the script must add a corresponding entry to the log file
# indicating the time, type of operation and file name. [The command to run the script must be added to
# crontab with a run frequency of one minute]

# echo "Enter path to the syncing directory: "  
# read path
                                       p1="/home/ser/Downloads/EPAM/HomeWorkBash"
# echo "Enter path to the directory where the copies of the files will be stored: "  
# read copy_path 
                                       p2="/home/ser/Documents/backup" 
									  # rm -r $p2
									   


if [ -z "$p1" ] || [ -z "$p2" ]; then
	echo "Parameters are wrong $(date +"%D %T")" >> $MYLOG
	exit 255;
fi

mkdir -p $p2
rsync -ah --log-file=$p2/backup.log $p1/ $p2