# To make sure a string will display as expected, we can format the result with the format() method.
# String format() method allows you to format selected parts of a string.
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method

# Add a placeholder where you want to display the price:
price = 49
print("The program costs {} dollars".format(price))
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

# В Python 3.6 появилась новая разновидность строк — f-строки.
# Если поставить перед строкой префикс f, в заполнители можно будет включить код, например имя переменной.

first_name = "Sergii"
father_name = "Victorovich"
age = 27
profession = "math teacher"
affiliation = "GitHub"
print(
    f"Hello, {first_name} {father_name}. You are {age}. You are a {profession}. You were a member of {affiliation}"
)
# Hello, Sergii Victorovich. You are 27. You are a math teacher. You were a member of GitHub
