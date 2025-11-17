amount_numbers = int(input("How many numbers do you want to enter: "))

user_set_1 = {
    int(input(f"Enter your {i+1} number in the first set: "))
    for i in range(amount_numbers)
}
user_set_2 = {
    int(input(f"Enter your {i+1} number in the second set: "))
    for i in range(amount_numbers)
}
print(f"Your first set: {user_set_1}")
print(f"Your second set: {user_set_2}")

union_set = user_set_1.union(user_set_2)
print(f"Union of the sets: {union_set}, sum = {sum(union_set)}")

intersection_set = user_set_1.intersection(user_set_2)
print(f"Intersection of two sets: {intersection_set}, sum = {sum(intersection_set)}")

difference_set = user_set_1.difference(user_set_2)
print(f"Print difference of two sets: {difference_set}, sum = {sum(difference_set)}")
