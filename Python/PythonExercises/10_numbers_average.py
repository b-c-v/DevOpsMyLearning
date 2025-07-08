total_sum = 0


def add_to_total(number):
    global total_sum
    total_sum += number
    return total_sum


for i in range(1, 6):
    number = int(input(f"Enter mark number {i}: "))
    add_to_total(number)

print(f"Total sum: {total_sum}")
print(f"Average: {total_sum/5}")
