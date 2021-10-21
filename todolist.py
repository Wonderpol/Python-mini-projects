import json

user_choice = -1

data = {'tasks': []}


def add_task():
    task_name = input("Type name of your task: ")
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
    try:
        with open("test.json") as json_file:
            data_json = json.load(json_file)

            for t in data_json['tasks']:
                data['tasks'].append({
                    "task_name": t['task_name'],
                    "completed": t['completed'],
                })

        json_file.close()
    except FileNotFoundError:
        return


def remove_task():
    task_name_to_remove = input("Type task name that you want to remove")
    filtered_data = filter(lambda task: task['task_name'] != task_name_to_remove, data['tasks'])
    data['tasks'] = list(filtered_data)


def mark_as_done():
    task_idx = 0
    for d in data['tasks']:
        print(str(task_idx) + ". " + d['task_name'])
        task_idx += 1

    task_idx_input = int(input("Task number you want to mark as done: "))

    if 0 <= task_idx_input <= len(data['tasks']) - 1:
        data['tasks'][task_idx_input]['completed'] = True
    else:
        print("There is no task with index: " + str(task_idx_input))
        return


load_tasks_to_data_dictionary()

while user_choice != 6:

    if user_choice == 1:
        print()
        show_tasks()
    elif user_choice == 2:
        print()
        add_task()
    elif user_choice == 3:
        mark_as_done()
        print()
    elif user_choice == 4:
        remove_task()
        print()
    elif user_choice == 5:
        print()
        save_tasks_to_file()
    else:
        print("You have to choose number from 1 to 6")

    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark as done")
    print("4. Remove task")
    print("5. Save changes to file")
    print("6. Exit")

    user_choice = int(input("Choose action to perform (number from 1 to 6): "))
    print()
