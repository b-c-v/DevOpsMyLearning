mark_list = []

username = input("What is your name?\n")

for i in range(5):
    mark = int(input("Enter your mark: "))
    mark_list.append(mark)

print(f"Hello {username}!")

marks_sum = sum(mark_list)
marks_average = marks_sum / 5

print("Summary of your marks is: ", marks_sum)
print("Average of your marks is: ", marks_average)
print("See your all subject marks:")
print(f"English = {mark_list[0]}")
print(f"AI = {mark_list[1]}")
print(f"Physics = {mark_list[2]}")
print(f"Computer = {mark_list[3]}")
print(f"Math = {mark_list[4]}")
