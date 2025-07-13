number = int(input("Enter any number: "))
number2 = int(input("Enter any number: "))
number += number2
print("+=", number)

number *= number2
print("*=", number)

number &= number2
print("&=", number)

number |= number2
print("|=", number)

number ^= number2
print("^=", number)

number >>= number2
print(">>=", number)

number <<= number2
print("<<=", number)

number /= number2
print("/=", number)

number //= number2
print("//=", number)

number **= number2
print("**=", number)

number %= number2
print("%=", number)


number -= number2
print("-=", number)

"""
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
