import csv

range_start = int(input("Enter the start of the range: "))
range_finish = int(input("Enter the finish of the range: "))

# Write each odd number as a new row in the CSV file
with open("tmp.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Odd numbers"])
    for number in range(range_start, range_finish):
        if number % 2 != 0:
            writer.writerow([number])
