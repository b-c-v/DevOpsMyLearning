data_list = [
    1,
    1.0,
    "any string 1",
    2,
    2.0,
    "another string 2",
    3,
    4,
    3.0,
    "1+sdf",
    True,
    False,
]

int_counter = 0
float_counter = 0
string_counter = 0
unrecognized_counter = 0

for i in data_list:
    if type(i) == int:
        int_counter += 1
    elif type(i) == float:
        float_counter += 1
    elif type(i) == str:
        string_counter += 1
    else:
        unrecognized_counter += 1

print(f"Integers: {int_counter}")
print(f"Floats: {float_counter}")
print(f"Strings: {string_counter}")
print(f"Unrecognized: {unrecognized_counter}")

# convert float in integers in the list
for i in range(len(data_list)):
    if type(data_list[i]) == float:
        data_list[i] = int(data_list[i])

print(f"List with replaced float in integers: {data_list}")
