start = int(input("Enter firs number: "))
end = int(input("Enter last number: "))
step = int(input("Enter a step: "))
if start < end and step < end:
    for i in range(start, end, step):
        print(i)
else:
    print("First number must be less then last number. Step should be less then last number!")
