#!/bin/bash
path=./example_log.log

command -v awk  >/dev/null 2>&1 || { echo >&2 "For working this script please install awk.  Aborting."; exit 1; }


# B. Using Apache log example create a script to answer the following questions:

# 1. From which ip were the most requests?
# grep -Eo "([0-9]{1,3}[\.]){3}[0-9]{1,3}" ~/Documents/EPAM/HomeWorkBash/example_log.log | sort | uniq -c | sort -rnk1 | awk 'NR==1{print $2}'


# 2. What is the most requested page?
# grep -Eo "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)" ~/Documents/EPAM/HomeWorkBash/example_log.log | sort | uniq -c | sort -rnk1 | awk 'NR==1{print $2}'

# 3. How many requests were there from each ip?
# grep -Eo "([0-9]{1,3}[\.]){3}[0-9]{1,3}" ~/Documents/EPAM/HomeWorkBash/example_log.log | sort | uniq -c | sort -rnk1 | awk '{print $2" : "$1}'

# 4. What non-existent pages were clients referred to?
# grep " 404 " ~/Documents/EPAM/HomeWorkBash/example_log.log | grep -E -o "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)" | sort | uniq

# 5. What time did site get the most requests?
# grep -Eo "[0-9]{2}\/[a-zA-Z]{3}\/[0-9]{4}(\:[0-9]{2}){2}" ~/Documents/EPAM/HomeWorkBash/example_log.log | sort | uniq -c | sort -rnk1 | awk 'NR==1{print $2}'

# 6. What search bots have accessed the site? (UA + IP)
grep "bot" $path > test.txt #| grep -E -o "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)" | sort | uniq
