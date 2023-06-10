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

# The range() Function. To loop through a set of code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)  # 0 1 2 3 4 5
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# Если переменная цикла не используется в теле цикла, то указывайте вместо нее символ нижнего подчеркивания _.
for _ in range(3):
    print('Hello')  # Hello Hello Hello

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
# Если первый параметр больше второго, то функция range() генерирует пустую последовательность. Например, range(10, 1) приводит к генерации пустой последовательности.
# Using the start parameter:
for x in range(2, 6):
    print('range start parameter', x)  # 2 3 4 5

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print('range increment the sequence -', x)  # 2 5 8 11 14 17 20 23 26 29

# Можно указать отрицательный шаг генерации (третий параметр), что приведет к генерированию убывающей последовательности.
# Старт последовательности (первый параметр) должен быть больше чем конец последовательности (второй параметр).
for i in range(5, 0, -1):
    print(i, end=' ')  # 5 4 3 2 1
# Если величина шага отрицательна и первый параметр меньше второго, то функция range() генерирует пустую последовательность.
# Например, вызов функции range(1, 10, -1) приводит к генерации пустой последовательности.

# Величина шага не может равняться нулю. Следующий код:
# range(1, 10, 0) приведет к ошибке ValueError: range() arg 3 must not be zero.

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
