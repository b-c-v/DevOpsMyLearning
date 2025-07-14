day = input("Enter any day of the week: ").lower()
holidays = {"saturday", "sunday"}

if day in holidays:
    print("It's a holiday")
else:
    print("It's a working day")
