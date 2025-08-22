alphabet = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
length = len(alphabet)
index = 0
max_width = 5  # Максимальное количество символов в строке

# Верхняя часть (расширяется до max_width)
for i in range(1, max_width + 1):
    if index >= length:
        break
    print("\t".join(alphabet[index : index + i]))
    index += i

# Нижняя часть (сужается обратно)
for i in range(max_width - 1, 0, -1):
    if index >= length:
        break
    print("\t".join(alphabet[index : index + i]))
    index += i
