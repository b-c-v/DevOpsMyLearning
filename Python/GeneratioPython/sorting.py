# Bubble sort
b = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
n = len(b)
for i in range(n - 1):
    flag = True
    for j in range(n - i - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
            flag = False
    if flag:
        break
print(b)

# Selection sort
s = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
sort = []
count = 0
while count < len(s):
    dmin = min(s)
    sort.append(dmin)
    s.remove(dmin)
count += 1
print(sort)

# Selection sort without list functions
sf = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
n = len(sf)
for i in range(n):
    mx_ind = n - 1 - i
    for j in range(n - i):
        if sf[j] > sf[mx_ind]:
            mx_ind = j
    sf[n - 1 - i], sf[mx_ind] = sf[mx_ind], sf[n - 1 - i]
print(sf)

# Insert sort
insert = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
n = len(insert)
for i in range(1, n):
    elem = insert[i]  # первый элемент из неотсортированной части списка
    j = i
    while j >= 1 and insert[j - 1] > elem:
        insert[j] = insert[j - 1]
        j -= 1
    insert[j] = elem
print(insert)
