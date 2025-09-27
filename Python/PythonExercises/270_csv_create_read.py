import csv

data_list = []

with open("tmp.csv", "w", newline="") as csvfile:
    write = csv.writer(csvfile)
    write.writerow(["Name", "Age", "Grade"])
    write.writerow(["Alice", 14, "9th"])
    write.writerow(["Bob", 15, "10th"])
    write.writerow(["Charlie", 13, "8th"])

with open("tmp.csv", "r") as csvfile:
    reade = csv.reader(csvfile)
    for row in reade:
        data_list.append(row)

print(f"Data saved in the list: {data_list}")
