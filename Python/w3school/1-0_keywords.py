# Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers:
"""
and         A logical operator
as          To create an alias
assert      For debugging
async       Define an asynchronous function
await       Wait for and get a result from an awaitable
break       To break out of a loop
case        Pattern in a match statement
class       To define a class
continue    To continue to the next iteration of a loop
def         To define a function
del         To delete an object
elif        Used in conditional statements, same as else if
else        Used in conditional statements
except      Used with exceptions, what to do when an exception occurs
False       Boolean value, result of comparison operations
finally     Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for         To create a for loop
from        To import specific parts of a module
global      To declare a global variable
if          To make a conditional statement
import      To import a module
in          To check if a value is present in a list, tuple, etc.
is          To test if two variables are equal
lambda      To create an anonymous function
match       Start a match statement (compare a value against cases)
None        Represents a null value
nonlocal    To declare a non-local variable
not         A logical operator
or          A logical operator
pass        A null statement, a statement that will do nothing
raise       To raise an exception
return      To exit a function and return a value
True        Boolean value, result of comparison operations
try         To make a try...except statement
while       To create a while loop
with        Used to simplify exception handling
yield       To return a list of values from a generator
"""

# yield
# The yield keyword turns a function into a function generator.
# The function generator returns an iterator.
# The code inside the function is not executed when they are first called, but are divided into steps, one step for each yield, and each step is only executed when iterated upon.
# Unlike the return keyword which stops further execution of the function, the yield keyword returns the result so far, and continues to the next step.


# Return three values from a function:
def myFunc():
    yield "Hello"
    yield 51
    yield "Good Bye"


x = myFunc()

for z in x:
    print(f"myFunc: {z}")


# The return value will be a list of values, one item for each yield.
# Note that the code inside the function is not executed when calling the function, it is only executed when the returned iterator is iterated upon:
y = 0


def myFunc():
    global y
    y = 10
    yield "Hello"
    y = 20
    yield "any value"
    y = 30
    yield "Good Bye"


x = myFunc()  # function is called:
print("y is still:", y)  # y is still 0

next(x)  # run the first iteration
print("y becomes:", y)  # y becomes: 10

next(x)  # run another iteration
print("y becomes:", y)  # y becomes: 20


next(x)  # run another iteration
print("y becomes:", y)  # y becomes: 30

# If you need to print value of yield, you must use a for loop or the next() function to iterate through the values returned by the generator function. If you try to print the generator function directly, it will not execute the code inside the function and will not return the values from yield, but instead will return a generator object:
print(myFunc())  # <generator object myFunc at 0x7f8bc8e5d0>

for value in myFunc():
    print(f"yield value with for loop: {value}")

# Also to print the value of yield, you can use the next() function to iterate through the values returned by the generator function:
x = myFunc()
print(f"yield value with next(): {next(x)}")  # Hello
print(f"yield value with next(): {next(x)}")  # any value
print(f"yield value with next(): {next(x)}")  # Good Bye


# можно использовать yield вместе с return без ошибки, если не вызывать next() после завершения генератора
#  return внутри генератора НЕ возвращает обычное значение, а вызывает StopIteration(value)
def myFuncReturn():
    yield "Hello"
    return "Value of return"


y = myFuncReturn()
print(next(y))  # Hello
# print(next(y)) # StopIteration: Value of return

# или обрабатывать StopIteration c помощью for цикла, который автоматически обрабатывает StopIteration и не вызывает ошибку:
for v in myFuncReturn():
    print(f"yield value: {v}")  # yield value: Hello

# или обрабатывать StopIteration с помощью try-except блока:
while True:
    try:
        print(next(y))  # Hello
    except StopIteration as e:
        print(
            f"Generator is exhausted. Return value: {e.value}"
        )  # Generator is exhausted. Return value: Text of return
        break
