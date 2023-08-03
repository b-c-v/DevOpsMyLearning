# Python allows for user input.
# That means we are able to ask the user for input.
# Python stops executing when it comes to the input() function, and continues when the user has given some input.

# The method is a bit different in Python 3.6 than Python 2.7.
# Python 3.6 uses the input() method.
# Python 2.7 uses the raw_input() method.

# The following example asks for the username, and when you entered the username, it gets printed on the screen:
# Python 3.6
username = input("Enter username:")
print("Username is: " + username)

# Python 2.7
# username = raw_input("Enter username:")
# print("Username is: " + username)

# Another way to print, and here no space is needed before "
print("Username is:", username)

print("Username is:", input())

# Ввести сразу несколько значений в одной строке и разбить их на разные переменные
v1, v2, v3 = input('Enter integer, string and float: ').split()
n1 = int(v1)
s1 = str(v2)
f1 = float(v3)
print('float -', f1)
print('string -', s1)
print('integer -', n1)
