# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x) # display the current date

# Date Output. When we execute the code from the example above the result will be:
# 2023-04-14 17:08:39.201288
# The date contains year, month, day, hour, minute, second, and microsecond.

"""
A reference of all the legal format codes:
Directive      Description                                                       Example
%a             Weekday, short version                                            Wed
%A             Weekday, full version                                             Wednesday
%w             Weekday as a number 0-6, 0 is Sunday                              3
%d             Day of month 01-31                                                31
%b             Month name, short version                                         Dec
%B             Month name, full version                                          December
%m             Month as a number 01-12                                           12
%y             Year, short version, without century                              18
%Y             Year, full version                                                2018
%H             Hour 00-23                                                        17
%I             Hour 00-12                                                        05
%p             AM/PM                                                             PM
%M             Minute 00-59                                                      41
%S             Second 00-59                                                      08
%f             Microsecond 000000-999999                                         548513
%z             UTC offset                                                        +0100
%Z             Timezone                                                          CST
%j             Day number of year 001-366                                        365
%U             Week number of year, Sunday as the first day of week, 00-53       52
%W             Week number of year, Monday as the first day of week, 00-53       52
%c             Local version of date and time      Mon Dec 31 17:41:00           2018
%C             Century                                                           20
%x             Local version of date                                             12/31/18
%X             Local version of time                                             17:41:00
%%             A % character                                                     %
%G             ISO 8601 year                                                     2018
%u             ISO 8601 weekday (1-7)                                            1
%V             ISO 8601 weeknumber (01-53)                                       01
"""
# The datetime module has many methods to return information about the date object.
# Here are a few examples, you will learn more about them later in this chapter:
# Return the year and name of weekday:

x = datetime.datetime.now()
print(x.year)  # 2023
print(x.strftime("%A"))  # Friday

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
x = datetime.datetime(2020, 5, 17)
print(x)  # 2020-05-17 00:00:00

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

# The strftime() method takes one parameter, format, to specify the format of the returned string:
# Display the name of the month:

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))  # June
