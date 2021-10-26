import random
import sys
import re
import requests

number_of_tries = 5
used_letters = []
user_word = []


def get_words_from_api():
    print("Downloading words")
    print()
    api_url = "https://random-word-api.herokuapp.com/word?number=50"
    response = requests.get(api_url)
    if response.status_code != requests.codes.ok:
        print("Something went wrong while downloading words")
        exit(-1)
    else:
        print("Completed")
        print()
        return response.json()


def find_indices(word, letter):
    indices = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indices.append(index)

    return indices


def show_info():
    print()
    print(user_word)
    print("Remaining number of tries: " + str(number_of_tries))
    print("Used letters: ", used_letters)
    print()


def validated_input(used_letters):
    pattern = r'[a-zA-Z]+'
    while True:
        letter = input("Type a letter: ")
        match = re.findall(pattern, letter)

        if len(match) == 0:
            print("You can input only letter (A-Z and a-z)")
        elif len(letter) != 1:
            print("You have to input only one letter. Try again")
        elif letter in used_letters:
            print("You've already used that letter")
        else:
            return letter


word = random.choice(get_words_from_api()).lower()
print("Your word consist of " + str(len(word)) + " letters")

for _ in word:
    user_word.append("_")

while True:
    letter = validated_input(used_letters)

    used_letters.append(letter)

    found_indices = (find_indices(word, letter))

    if len(found_indices) == 0:
        print()
        print("Letter " + '"' + letter + '"' + " is not correct")
        number_of_tries -= 1

        if number_of_tries == 0:
            print()
            print("The end, you lost")
            sys.exit(0)
    else:
        for index1 in found_indices:
            user_word[index1] = letter

        if "".join(user_word) == word:
            print("Good Job, you won")
            sys.exit(0)

    show_info()
