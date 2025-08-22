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
print(15 / 4)  # 3.75

# // (целочисленное деление) всегда округляет результат в сторону минус бесконечности (вниз по числовой прямой), а не просто отбрасывает дробную часть.
# a // b == floor(a/b)
# floor() — это округление вниз до ближайшего целого числа.
# 15 / 4 = 3.75, целочисленное деление 15 // 4 = 3 так как 3.75 округляется вниз до 3 — в этом случае округление совпадает с отбрасыванием дробной части, потому что число положительное
print("a // b =", 15 // 4)  # 3

# -15 / 4 = -3.75 округление вниз (в сторону минус бесконечности): -4
print("a // -b =", 15 // -4)  # -4

print("-a // b =", -15 // 4)  # -4


# % возвращает остаток от деления первого числа на второе
# a % b = a - (b * floor(a / b)) формула, по которой вычисляется результат
# 15 % 4 == 15 - (4 * floor(3.75))
# 15 % 4 == 15 - 12
print("a % b =", 15 % 4)  # 3

# 15%-4 == 15 - (-4 * floor(-3.75))
# 15%-4 == 15 - 16
print("a % -b", 15 % -4)  # -1

# результат оператора % всегда имеет тот же знак, что и делитель
print("-a % b =", -15 % 4)  # 1


# Assignment operators are used to assign values to variables:
"""
   Operator      Example   Same As       Name
   =             x = 5     x = 5         Assignment
   +=            x += 3    x = x + 3     Addition assignment
   -=            x -= 3    x = x - 3     Subtraction assignment
   *=            x *= 3    x = x * 3     Multiplication assignment
   /=            x /= 3    x = x / 3     Division assignment
   %=            x %= 3    x = x % 3     Modulus assignment
   //=           x //= 3   x = x // 3    Floor division assignment
   **=           x **= 3   x = x ** 3    Exponentiation assignment
   &=            x &= 3    x = x & 3     Bitwise AND assignment
   |=            x |= 3    x = x | 3     Bitwise OR assignment
   ^=            x ^= 3    x = x ^ 3     Bitwise XOR assignment
   >>=           x >>= 3   x = x >> 3    Right shift assignment
   <<=           x <<= 3   x = x << 3    Left shift assignment
"""
x = 5
x &= 3
# 5 в двоичной системе → 0101
# 3 в двоичной системе → 0011
# Операция & возвращает 1 только если оба бита равны 1, иначе 0
"""
  0101 (5)
& 0011 (3)
  ----
  0001 (1)
"""
print("&=", x)  # 1

# Операция | возвращает 1, если хотя бы один бит равен 1:
x = 5
x |= 3
"""
  0101 (5)
| 0011 (3)
  ----
  0111 (7)
"""
print("|=", x)  # 7

# Операция ^ возвращает 1, если биты разные, и 0, если одинаковые:
x = 5
x ^= 3
"""
  0101 (5)
^ 0011 (3)
  ----
  0110 (6)
  """
print("^=", x)  # 6

# >>= (Сдвиг вправо) — эквивалентно целочисленному делению на 2ⁿ (где n — количество сдвигов).
# Операция >> сдвигает биты вправо, отбрасывая младшие биты:
x = 8  # 1000
x >>= 2  # 0010 два нуля добавляются слева, два бита справа отбрасываются
print(">>=", x)  # 2

# <<= (Сдвиг влево) — эквивалентно умножению на 2ⁿ (где n — количество сдвигов).
# Операция << сдвигает биты влево, добавляя нули справа
x = 2  # 0010
x <<= 3  # 10000 сдвигаем биты влево на 3 (три нуля добавлены справа)
print("<<=", x)  # 16

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
"""
Другое объяснение:
Оператор not в логике тоже, что и смена знака в арифметике. And аналог умножения (*). Or аналог сложения (+). Соответственно и приоритеты те же.
Например, True = 1, а False = 0.
a = 0 (False)
b = 1 (True)
a or  b ==> a + b ==> 0 + 1 = 1 (True)
a and b ==> a * b ==> 0 * 1 = 0 (False)

a = 0 (False)
b = 1 (True)
c = 0 (False)

not a or b and c:
1) not a              ==> not 0 (False)      ==> 1 (True)
2) b and c            ==> b * c              ==> 1 * 0 = 0 (False)
3) not a or (b and c) ==> not a + (b * c)    ==> 1 + 0 = 1 (True)


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
