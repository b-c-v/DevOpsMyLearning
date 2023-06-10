"""
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""

# Arithmetic operators are used with numeric values to perform common mathematical operations:
"""
   +     Addition           x + y
   -     Subtraction        x - y
   *     Multiplication     x * y
   /     Division           x / y
   %     Modulus            x % y
   **    Exponentiation     x ** y   # Возведение в степень
   //    Floor division     x // y   # Целочисленное деление
"""
print(15/4)          # 3.75
print(3/5)           # 0.6
print(15 % 4)        # 3
print(3 % 5)         # 3
print(-15 % 4)         # 1
print(3 % -5)          # -2
print(-4 % 5)          # 1

# Floor division operator will divide the first argument by the second and round the result down to the nearest whole number.
# The result of regular division (using the / operator) is 15/4=3.75, but using // has floored down to 3
print(15//4)       # 3
# When an operand is negative, floor division will return the largest integer less than or equal to the result of regular division.
print(-15 // 4)    # -4


# Assignment operators are used to assign values to variables:
"""
   Operator      Example   Same As
   =             x = 5     x = 5
   +=            x += 3    x = x + 3
   -=            x -= 3    x = x - 3
   *=            x *= 3    x = x * 3
   /=            x /= 3    x = x / 3
   %=            x %= 3    x = x % 3
   //=           x //= 3   x = x // 3
   **=           x **= 3   x = x ** 3
   &=            x &= 3    x = x & 3
   |=            x |= 3    x = x | 3
   ^=            x ^= 3    x = x ^ 3
   >>=           x >>= 3   x = x >> 3
   <<=           x <<= 3   x = x << 3
"""

# Comparison operators are used to compare two values:
""" 
   ==     Equal                        x == y
   !=     Not equal                    x != y
   >      Greater than                 x > y
   <      Less than                    x < y
   >=     Greater than or equal to     x >= y
   <=     Less than or equal to        x <= y
"""
"""
Операторы сравнения в Python можно объединять в цепочки.
Например, a == b == c или 1 <= x <= 10
"""

# Logical operators are used to combine conditional statements:
"""
and   Returns True if both statements are true                  x < 5 and  x < 10
    
    a        b       a and b
    False    False   False
    False    True    False
    True     False   False
    True     True    True

or    Returns True if one of the statements is true             x < 5 or x < 4
    
    a       b       a or b
    False   False   False
    False   True    True
    True    False   True
    True    True    True

not   Reverse the result, returns False if the result is true   not(x < 5 and x < 10)

    a       not a
    False   True
    True    False

Приоритет выполнения следующий:

    в первую очередь выполняется логическое отрицание not;
    далее выполняется логическое умножение and;
    далее выполняется логическое сложение or.

Операторы, and и or, вычисляются по укороченной схеме.
    Если условие слева от оператора and является ложным, то условие справа от него не проверяется.
    Если условие слева от оператора or истинное, то условие справа от него не проверяется.

"""

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
"""
   is        Returns True if both variables are the same object       x is y
   is not    Returns True if both variables are not the same object   x is not y
"""

# Membership operators are used to test if a sequence is presented in an object:
"""
   in        Returns True if a sequence with the specified value is present in the object        x in y
   not in    Returns True if a sequence with the specified value is not present in the object    x not in y
"""

# Bitwise operators are used to compare(binary) numbers:
"""
   Operator  Name                  Description                                                                                              Example
   &         AND                   Sets each bit to 1 if both bits are 1                                                                    x & y
   |         OR                    Sets each bit to 1 if one of two bits is 1                                                               x | y
   ^         XOR                   Sets each bit to 1 if only one of two bits is 1                                                          x ^ y
   ~         NOT                   Inverts all the bits                                                                                     ~x
   <<        Zero fill left shift  Shift left by pushing zeros in from the right and let the leftmost bits fall off                         x << 2
   >>        Signed right shift    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off  x >> 2
"""

# The precedence order is described in the table below, starting with the highest precedence at the top:
# If two operators have the same precedence, the expression is evaluated from left to right.
"""
   ()                                       Parentheses
   **                                       Exponentiation
   +x - x  ~x                               Unary plus, unary minus, and bitwise NOT
   * / // %                                 Multiplication, division, floor division, and modulus
   + -                                      Addition and subtraction
   << >>                                    Bitwise left and right shifts
   &                                        Bitwise AND
   ^                                        Bitwise XOR
   |                                        Bitwise OR
   == != > >= < <= is is not in not in      Comparisons, identity, and membership operators
   not                                      Logical NOT
   and                                      AND
   or                                       OR
"""
# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:
print(5 + 4 - 7 + 3)  # 5
