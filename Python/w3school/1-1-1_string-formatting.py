# To make sure a string will display as expected, we can format the result with the format() method.
# String format() method allows you to format selected parts of a string.
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# Если поставить перед строкой префикс f, в заполнители можно будет включить код, например имя переменной.
age = 36
txt = f"My name is John, and I am {age}"
print(txt)  # My name is John, and I am 36

first_name = "Sergii"
father_name = "Victorovich"
age = 27
profession = "math teacher"
affiliation = "GitHub"
print(
    f"Hello, {first_name} {father_name}. You are {age}. You are a {profession}. You were a member of {affiliation}"
)
# Hello, Sergii Victorovich. You are 27. You are a math teacher. You were a member of GitHub

# A placeholder can also include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  # The price is 59.00 dollars

# You can also format a value directly without keeping it in a variable:
# Display the value 95 with 2 decimals:
txt = f"The price is {95:.2f} dollars"
print(txt)  # The price is 95.00 dollars

# Use a comma as a thousand separator:
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)  # The price is 59,000 dollars

"""
Formatting    Types
:<            left aligns the result (within the available space)
:>            right aligns the result (within the available space)
:^            center aligns the result (within the available space)
:=            places the sign to the left most position
:+            use a plus sign to indicate if the result is positive or negative
:-            use a minus sign for negative values only
:             use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,            use a comma as a thousand separator
:_            use a underscore as a thousand separator
:b            binary format
:c            converts the value into the corresponding unicode character
:d            decimal format
:e            scientific format, with a lower case e
:E            scientific format, with an upper case E
:f            fix point number format
:F            fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g            general format
:G            general format (using a upper case E for scientific notations)
:o            octal format
:x            hex format, lower case
:X            hex format, upper case
:n            number format
:%            percentage format
"""

# ***Perform operations in F-Strings***
# You can perform Python operations inside the placeholders.
# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)  # The price is 1180 dollars

# Perform math operations on variables. Add taxes before displaying the price:
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)  # The price is 73.75 dollars

# You can perform if...else statements inside the placeholders:
# Return "Expensive" if the price is over 50, otherwise return "Cheap":
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)  # It is very Cheap

# ***Execute functions in F-Strings***
# You can execute functions inside the placeholder.
# Use the string method upper()to convert a value into upper case letters:
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)  # I love APPLES


# The function does not have to be a built-in Python method, you can create your own functions and use them.
# Create a function that converts feet into meters:
def myconverter(x):
    return x * 0.3048


txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)  # The plane is flying at a 9144.0 meter altitude


# Before Python 3.6 we had to use the format() method.
# Add a placeholder where you want to display the price:
price = 49
print("The program costs {} dollars".format(price))  # The program costs 49 dollars
txt = "The price is {} dollars"
print(txt.format(price))  # The price is 49 dollars

# You can add parameters inside the curly brackets to specify how to convert the value:
# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
print(txt.format(price))  # The price is 49.00 dollars

# Check out all formatting types in our String format() Reference.
# If you want to use more values, just add more values to the format() method:
# print(txt.format(price, item_number, count))

# And add more placeholders:
quantity = 3
item_number = 567
price = 49
my_order = "I want {} pieces of item number {} for {:.2f} dollars."
# I want 3 pieces of item number 567 for 49.00 dollars.
print(my_order.format(quantity, item_number, price))

# Для наглядности и гибкости форматирования можно использовать порядковый номер в заполнителе: {0}, {1}, {2},....
# Такой номер определяет позицию параметра, переданного методу format (нумерация начинается с нуля):
age = 27
name = "Sergii"
profession = "math teacher"
txt = "My name is {0}, I am {1}, I work as a {2}".format(name, age, profession)
print(txt)  # My name is Sergii, I am 27, I work as a math teacher

print("My name is {0}-{0}-{0}".format(name))  # My name is Sergii-Sergii-Sergii

# Index Numbers. You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
quantity = 3
item_number = 567
price = 49
my_order = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# I want 3 pieces of item number 567 for 49.00 dollars.
print(my_order.format(quantity, item_number, price))

# Also, if you want to refer to the same value more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))  # His name is John. John is 36 years old.

# Named Indexes. You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
my_order = "I have a {carname}, it is a {model}."
# I have a Ford, it is a Mustang.
print(my_order.format(carname="Ford", model="Mustang"))

# %-formatting called "old style" formatting. It uses the % operator to format strings.
# %s - string
# %i - integer
# %f - floating point decimal
# %x - hexadecimal integer
# %o - octal integer
# %% - literal percent sign
print("My name is %s and this is my age %i" % ("Sergii", 19))
# My name is Sergii and this is my age 19
