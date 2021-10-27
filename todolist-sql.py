import datetime
import sqlite3
import time

connection = sqlite3.connect("todo.db")
date_format = "%d-%m-%Y"


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text, is_completed BOOL, task_begin_date text, task_end_date text)""")
    except:
        pass


def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task, is_completed, task_begin_date, task_end_date FROM task""")
    res = cur.fetchall()

    if len(res) < 1:
        print("Your task list is empty")
    else:
        for task in res:
            print(str(task[0]) + ". " + task[1])
            print("Task begin date: " + task[3])
            print("Task end date: " + task[4])
            if task[2] == 0:
                print("Task is not completed\n")
            else:
                print("Task is completed\n")


def validate_date(date):
    if not datetime.datetime.strptime(date, date_format):
        return ValueError


def compare_two_dated(date1, date2, date_format):
    if time.strptime(date1, date_format) > time.strptime(date2, date_format):
        return True
    else:
        return False


def info_about_date_format():
    print("Date should be in format DD-MM-YYYY\n")


def add_task(connection):
    task_name = input("Type name of your task: ")

    while True:
        begin_date = input("Input begin task date: ")
        try:
            validate_date(begin_date)
        except ValueError:
            info_about_date_format()
        end_date = input("Input end task date: ")
        try:
            validate_date(end_date)
        except ValueError:
            info_about_date_format()

        if compare_two_dated(begin_date, end_date, date_format):
            print("Date of task end can't be older than task begin date")
            continue

        else:
            break

    cur = connection.cursor()
    cur.execute("""INSERT INTO task(task, is_completed, task_begin_date, task_end_date) VALUES(?,?,?,?)""",
                (task_name, False, begin_date, end_date))
    connection.commit()


def mark_as_done(connection):
    show_tasks(connection)
    task_index = input("Type task index that you have completed: ")
    cur = connection.cursor()
    cur.execute("""UPDATE task SET is_completed = ? WHERE rowid = ?""", (True, task_index))
    connection.commit()


def remove_task(connection):
    show_tasks(connection)

    task_index = input("Type task index that you want to remove: ")

    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM TASK WHERE rowid = ?""", (task_index,)).rowcount
    connection.commit()

    if rows_deleted == 0:
        print("Something went wrong while removing the task")
    else:
        print("Task has been removed successfully")


if connection is not None:
    create_table(connection)
else:
    print("Error while creating the database connection")

while True:
    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark as done")
    print("4. Remove task")
    print("5. Exit")

    user_choice = int(input("Choose action to perform (number from 1 to 5):\n"))

    if user_choice == 1:
        print()
        show_tasks(connection)
    elif user_choice == 2:
        print()
        add_task(connection)
    elif user_choice == 3:
        mark_as_done(connection)
        print()
    elif user_choice == 4:
        remove_task(connection)
        print()
    elif user_choice == 5:
        connection.close()
        print("Good bye")
        break
    else:
        print("You have to choose number from 1 to 5")
