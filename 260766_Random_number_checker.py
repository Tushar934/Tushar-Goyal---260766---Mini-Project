import random
from os import path
attempts_list = []


def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score")
    else:
        print("Currently highest score is {} attempts".format(min(attempts_list)))


def file_input():
    for i in attempts_list:
        if path.exists("number_guessing.txt"):
            f = open("number_guessing.txt", "a")
            f.write("New Guessing number in the game is {}\n".format(str(i)))
            print(" ")
            f.close()
        else:
            f = open("number_guessing.txt", "w")
            f.write("The game of guesses presents \nGuessing Number in the game is {}\n".format(str(i)))
            print(" ")
            f.close()


def start_game():
    random_number = int(random.randint(1, 10))
    print("Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hello, {}, Interested to play the guessing game? (Yes/No) ".format(player_name))
# Where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes" or wanna_play.upper() == "YES":
        try:
            guess = input("Choose a number (1 and 10) ")
            if int(guess) < 1 or int(guess) > 10:  # user input range
                raise ValueError("Guess Number within the given range")
            if int(guess) == random_number:  # check user input with the number generator
                print("Nice Playing!")
                attempts += 1
                attempts_list.append(attempts)
                file_input()
                print("It took you {} attempts".format(attempts))
                play_again = input("Interested to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower guess")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher guess")
                attempts += 1
        except ValueError as err:   # Exception handler
            print("Invalid value. (Try again...)")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")


if __name__ == '__main__':
    start_game()