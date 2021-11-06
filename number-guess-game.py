import random

menu_options = {
    1: "Guess the number chosen by computer",
    2: "Let the computer guess the number",
    3: "Exit"
}


def show_menu():
    for key in menu_options.keys():
        print(f"{key}. {menu_options[key]}")


def computer_guess_number():
    while True:
        try:
            number_to_guess: int = int(input("Enter the number to guess by computer: "))
        except ValueError:
            print("You can use only digits")
            continue
        break
    computer_guess(number_to_guess)


def guess(x: int):
    random_number: int = random.randint(1, x)
    guessed_number: int = 0
    while guessed_number != random_number:
        try:
            guessed_number = int(input(f"Guess a number between 1 and {x}: "))
        except ValueError:
            print("You can use only digits")
            continue
        if guessed_number < random_number:
            print("Sorry, guess again. Too low.")
        elif guessed_number > random_number:
            print("Sorry, guess again. Too high.")

    print(f"You've guessed the number {guessed_number}")


def computer_guess(x: int):
    low_number: int = 1
    high_number: int = x
    feedback: str = ""
    while feedback != "c":
        if low_number != high_number:
            guessed_number_by_computer: int = random.randint(low_number, high_number)
        else:
            guessed_number_by_computer = low_number
        feedback: str = input(f"Is {guessed_number_by_computer} to high (H), too low (L) or correct (C): ").lower()
        if feedback == "h":
            high_number = guessed_number_by_computer - 1
        elif feedback == "l":
            low_number = guessed_number_by_computer + 1

    print(f"Computer guessed your number correctly: {str(guessed_number_by_computer)}")


if __name__ == "__main__":
    while True:
        show_menu()
        option: int = -1
        try:
            option: int = int(input("Enter your choice: "))
        except ValueError:
            print("Wrong choice. Please enter a number")

        if option == 1:
            guess(50)
        elif option == 2:
            computer_guess_number()
        elif option == 3:
            print("Thank you for playing. Good bye.")
            exit()
        else:
            print("Invalid option. Enter a number from 1 to 3")