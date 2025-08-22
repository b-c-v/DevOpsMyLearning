user_string = input("Enter any sentence: ")

odd_list = []
even_list = []

for i in range(len(user_string)):
    if i % 2 == 0:
        even_list.append(user_string[i])
    else:
        odd_list.append(user_string[i])

print(f"Characters that are present an odd index number: {odd_list}")
print(f"Characters that are present an even index number: {even_list}")
