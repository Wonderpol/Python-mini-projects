import json

user_choice = -1

data = {'tasks': []}


def add_task():
    task_name = input("What is your task?")
    priority = int(input("Priority of task from 1 to 3 (1 is low, 2 is medium, 3 is high)"))
    if priority < 1 or priority > 3:
        print("Priority must be from 1 to 3")
        return
    data['tasks'].append({
        "task_name": task_name,
        "completed": False,
    })


def save_tasks_to_file():
    with open("test.json", "w") as json_write_file:
        json.dump(data, json_write_file)


def show_tasks():
    for d in data['tasks']:
        print("Task: " + d['task_name'])
        print("Completed: " + str(d['completed']))
        print()


def load_tasks_to_data_dictionary():
    with open("test.json") as json_file:
        data_json = json.load(json_file)
        for t in data_json['tasks']:
            data['tasks'].append({
                "task_name": t['task_name'],
                "completed": t['completed'],
            })

    json_file.close()


load_tasks_to_data_dictionary()

while user_choice != 5:

    if user_choice == 1:
        print()
        show_tasks()
    elif user_choice == 2:
        print()
        add_task()
    elif user_choice == 3:
        # My problem
        # mark_as_completed()
        print()
    elif user_choice == 4:
        # My problem
        # delete_task()
        print()
    elif user_choice == 5:
        print()
        save_tasks_to_file()
    else:
        print("You have to choose number from 1 to 5")

    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark as done")
    print("4. Remove task")
    print("5. Save changes to file")
    print("5. Exit")

    user_choice = int(input("Choose action to perform (number from 1 to 5): "))
    print()
