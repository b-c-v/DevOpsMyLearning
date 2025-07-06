# With the while loop we can execute a set of statements as long as a condition is true.

# Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1

# Note: remember to increment i, or else the loop will continue forever.
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# The break Statement. With the break statement we can stop the loop even if the while condition is true:
# Exit the loop when i is 3:
i = 1
while i < 6:
    print("break -", i)  # 1 2 3
    if i == 3:
        break
    i += 1

# The continue Statement. With the continue statement we can stop the current iteration, and continue with the next:
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print("continue -", i)  # 1 2 3 4 5 6

# The else Statement.With the else statement we can run a block of code once when the condition no longer is true:
# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")  # 1 2 3 4 5 i is no longer less than 6


# Two conditional expressions, A and B, that it needs to evaluate. The and operator says to evaluate them separately and then consider their results as a whole. If (and only if) both A and B are true, then the loop body will execute. If even one of them is false, then the entire while statement evaluates to false and the loop terminates.

# цикл будет работать до тех пор, пока пользователь не введет слово хватит или конец
word = input()
while (word != "хватит") and (word != "конец"):
    print("and -", word)
    word = input()

# цикл будет работать до тех пор, пока пользователь не введет слово хватит или конец
word = input()
while not (word == "хватит" or word == "конец"):
    print("not -", word)
    word = input()

# Цикл будет работать бесконечно, поскольку блок кода выполняется в том случае если слева или справа от  or появляется значение True.
# Если первое значение от or истинно (True) то второе даже не проверяется и условие считается выполненным.
while (word != "хватит") or (word != "конец"):
    print("or -", word)
    word = input()