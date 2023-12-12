# Guessing Game project
# number 1- 100 X
# user has two modes of difficulty, "easy" and "hard"  X
# easy gives 10 guesses and hard gives 5  X
# User is asked to "Make a guess: "
# User is provided input on whether number is too high or low
# User then asked to "Guess again: "
# Notified of number of attempts remaining
# returns to "Make a guess: prompt"
# If correct number is guessed, print "You got it! The answer was <blank>"
# if user runs out of guesses, print "You've run out of guesses, you lose."
import os
import random
from Guessing_Game_Art import logo
random_number = ""
def retry():
    retry = input("Would you like to play again? Y or N: ")
    if retry.lower() == "y":
        os.system('cls')
        guessing_game()
    else:
        print("Goodbye!")
def guessing_game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(0, 101)
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
    guesses = ""
    if difficulty == "easy":
        guesses = 10
        print(f"You have {guesses} attempts remaining to guess the number.")
    if difficulty == "hard":
        guesses = 5
        print(f"You have {guesses} attempts remaining to guess the number.")

    # print(f"The number is {random_number}")
    # print(guesses)

    while guesses != 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it!  The answer was {random_number}.")
            retry()

        elif guess > random_number:
            guesses -= 1
            print("Too High.")
            print("Guess again.")
            print(f"You have {guesses} attempts remaining to guess the number.")
        elif guess < random_number:
            guesses -= 1
            print("Too Low.")
            print("Guess again.")
            print(f"You have {guesses} attempts remaining to guess the number.")
        if guesses == 0:
            print("You've run out of guesses, you lose.")
            retry()
guessing_game()
