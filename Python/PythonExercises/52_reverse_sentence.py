sentence = input("Please enter any sentence: ")
reverse = sentence[::-1]

print('Your reverse string is: "', reverse, '"')

# reverse string with for loop
reverse_for = ""

for i in sentence:
    reverse_for = i + reverse_for

print('Your reversed string using a for loop is: "', reverse_for, '"')
