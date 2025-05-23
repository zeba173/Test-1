#Number guessing game
import random
number = random.randint(1,100)
#guess_number = int(input('Guess the number between 1 to 100: '))
while True:
    guessed_number = int(input('Guess the number between 1 to 100: '))
    if guessed_number > number:
        print('Too high!')
    elif guessed_number < number:
        print('Too low!')
    else:
        print('Congratulations! You guessed the number.')
        break
    
     