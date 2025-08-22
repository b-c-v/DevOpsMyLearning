mark_list = []

username = input("What is your name?\n")

amount_marks = int(input("How many marks do you want to enter: "))

for i in range(amount_marks):
    mark = int(input("Enter your mark: "))
    mark_list.append(mark)

# sorted() не меняет оригинальный список, а просто делает отсортированную копию  в отличии от sort()
sorted_list = sorted(mark_list, reverse=True)

print(f"Hello {username}!")
print(f"You current marks are: {mark_list}!")
print(f"Second mark is {sorted_list[1]}")
