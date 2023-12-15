import os
import random
from Guessing_Game_Art import logo



def retry():
    retry = input("Would you like to play again? Y or N: ")
    if retry.lower() == "y":
        os.system('cls')
        guessing_game()
    elif retry.lower() == "n":
        print("Goodbye!")
        return
def guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
    guesses = ""
    if difficulty == "easy":
        guesses = 10
        print(f"You have {guesses} attempts remaining to guess the number.")
    if difficulty == "hard":
        guesses = 5
        print(f"You have {guesses} attempts remaining to guess the number.")

    while guesses != 0:
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it!  The answer was {random_number}.")
            guesses = 0
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
