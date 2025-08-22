from datetime import datetime

first_date = input("Please enter the first date in the format dd.mm.yyyy: ")
second_date = input("Please enter the second date in the format dd.mm.yyyy: ")

format_first_date = datetime.strptime(first_date, "%d.%m.%Y")
format_second_date = datetime.strptime(second_date, "%d.%m.%Y")

difference = format_second_date - format_first_date
print(f"Between {first_date} and {second_date} are {difference.days} days!")
print(f"Between {first_date} and {second_date} are {difference.days * 24} hours!")