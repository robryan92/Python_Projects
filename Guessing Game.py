secret_number = 16
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess the number: '))
    guess_count += 1
    if guess == secret_number:
        print('You guessed my number!')
        break
else:
    print('Sorry, you did not guess my magic number')
restart = input('Do you want to try again?: ')
while restart.upper() == 'YES':
    continue

