import datetime
import time

answer = input("Do you want to get current date Y/n: ")

if answer == "n":
    print("OK, thank you!")
else:
    print(datetime.datetime.now())
    # Current time in milliseconds
    # time.time() returns the current time in seconds as a float.
    current_time_milliseconds = int(time.time() * 1000)
    print(f"Current time in milliseconds is: {current_time_milliseconds}")
