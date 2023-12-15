from random import randint
from Guessing_Game_Art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def restart():
    retry = input("Would you like to start over? Y or N: ")
    if retry.lower() == "y":
        game()
    else:
        print("Goodbye")
        return

def check_answer(guess, answer, turns):
    """Checks answer against guess, returns number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You've got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty, easy or hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            restart()
            return

game()

