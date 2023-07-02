# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# The for loop does not require an indexing variable to set beforehand.

# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String. Even strings are iterable objects, they contain a sequence of characters:
# Loop through the letters in the word "banana":
for x in "banana":
    print('Loop through the letters -', x)

# The break Statement. With the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("break -", x)  # apple banana
    if x == "banana":
        break

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print('break before the print -', x)  # apple

# The continue Statement. With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print('continue -', x)  # apple cherry

# Else in For Loop. The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print('else in for -', x)
else:
    print("Finally finished!")  # 0 1 2 3 4 5 Finally finished!

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x == 3:
        break
    print('break -', x)  # 0 1 2
else:
    print("Finally finished!")

# Nested Loops. A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        # red apple red banana red cherry big apple big banana big cherry tasty apple tasty banana tasty cherry
        print(x, y)

# The pass Statement. for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass
