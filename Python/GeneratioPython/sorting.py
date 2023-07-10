#bubble sort
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
for i in range(n-1):
    flag = True
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = False
        if flag:
            break
print('bubble sort -', a)


#selection sort
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
sort = []
count = 0
while count < len(a):
    sort.append(min(a))
    a.remove(min(a))
count += 1
print('selection sort -', sort)
# selection sort (without functions)
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
for i in range(n):
    mx_ind = n - 1 - i
    for j in range(n - i):
        if a[j] > a[mx_ind]:
            mx_ind = j
    a[n - 1 - i], a[mx_ind] = a[mx_ind], a[n - 1 - i]
print('selection sort 2 -', a)


#Insert sort
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
for i in range(1, n): 
    elem = a[i]  # первый элемент из неотсортированной части списка
    j = i
    while j >= 1 and a[j - 1] > elem: 
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem
print('insert sort', a)
