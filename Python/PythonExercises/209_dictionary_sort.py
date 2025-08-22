user_dict = {}


def add_user_info():
    user_dict["name"] = input("Enter your name: ")
    user_dict["address"] = input("Enter your email: ")
    user_dict["contact"] = input("Enter your phone: ")
    user_dict["birth"] = input("Enter year of birth: ")
    print("Your current data: ", user_dict)
    return user_dict


sorted_dict_keys = dict(sorted(add_user_info().items()))
print(f"Sort by keys: {sorted_dict_keys}")


# sort by values
# из add_user_info().items() приходит кортеж (key, value). item[0] - это ключ, item[1] - это значение
def get_value(item):
    return item[1]


# Sort using the function
# key=get_value передает функцию как объект, sorted() сам будет вызывать её для каждого элемента списка
# если написать key=get_value(), Python сначала выполнит функцию и вернёт результат
sorted_dict_values = dict(sorted(add_user_info().items(), key=get_value))
print(f"Sort by values: {sorted_dict_values}")
