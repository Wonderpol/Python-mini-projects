expenses = []

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def show_menu(menu: dict):
    for key in menu.keys():
        print(f"{key}. {menu[key]}")


def show_expenses(month: int):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f"{months[month]}: {expense_amount} USD - {expense_type} ")


def add_expense(month: int):
    expense_amount = int(input("Enter amount in [USD]: "))
    expense_type = input("Enter type of the expense e.g food, house etc.: ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month: int):
    total_expenses_in_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    total_expenses_all_months = sum(expense_amount for expense_amount, _, _ in expenses)
    average_expense_this_month = total_expenses_in_this_month / number_of_expenses_this_month
    average_expense_all = total_expenses_all_months / len(expenses)

    print("\n Statistics in this mount [USD]: \n")
    print(total_expenses_in_this_month)
    print("\n Average expense in this mount [USD]: \n")
    print(average_expense_this_month)
    print("\n Overall statistics [USD]: \n")
    print(total_expenses_all_months)
    print("\n Average expense in this year [USD]: \n")
    print(average_expense_all)


if __name__ == "__main__":

    menu_options = {
        0: "Change month",
        1: "Show all expenses",
        2: "Add expense",
        3: "Statistics"
    }

    while True:
        month = int(input("Enter a month from 1-12: "))

        if month == 0:
            break

        while True:
            show_menu(menu_options)
            choice = int(input("Enter a number from 1-3 to perform an action: "))

            if choice == 0:
                break
            elif choice == 1:
                show_expenses(month)
            elif choice == 2:
                add_expense(month)
            elif choice == 3:
                show_stats(month)
            else:
                exit(-1)
