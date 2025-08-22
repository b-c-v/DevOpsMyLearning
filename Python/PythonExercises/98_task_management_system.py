task_list = ["ser", "ser2", "ser3"]


def hello_message():
    print("Welcome to the task manager! What do you want to do: ")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    selection = int(input("Please enter what do you want to do: "))
    return selection


def add_task():
    task = input("Please enter a task to add: ")
    task_list.append(task)


def view_tasks(task_list):
    print("Your tasks:")
    for i, task in enumerate(task_list):
        print(f"{i}\t{task}")


def delete_task():
    view_tasks(task_list)
    task_number = int(
        input("Please enter number of the task that you want to delete: ")
    )
    if task_number <= len(task_list):
        task_list.pop(task_number)
    else:
        print("You select wrong task number!")


answer = "y"

while answer.lower() == "y":
    choice = hello_message()
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks(task_list)
    elif choice == 3:
        delete_task()
    else:
        print("You made wrong choice!")
    answer = input("Do you want to change your data Y/n? ")
else:
    print("Your data saved. Thank you!")


print(task_list)
