sentence = input("Please enter any sentence: ")
start = int(input("Please enter a starting number: "))
end = int(input("Please enter an ending number: "))
if start > 0 and start < end and end < len(sentence):
    reverse_substring = sentence[start:end][::-1]
    print(f"Your reverse substring is: {reverse_substring}")
else:
    print("You entered the wrong coordinates.")
