#this is gonna be a about scope too
#Scope is about where the vars can be access
import random

print('Welcome to the guessing game')
lifes = 5
if(input('What mode you want? "easy" or "hard"? ')=='easy'):
    lifes = 10
numberToGuess = random.randint(0,101)
victory = False
while( not victory and lifes >0 ):
    numberGuessed = int(input(f'You have {lifes} left, Guess a number: '))
    if(numberGuessed == numberToGuess):
        victory = True
    else:
        if(numberGuessed < numberToGuess):
            print('number too low')
        else:
            print('number too high')
        lifes -= 1
if victory:
    print('you Won the number to guess was ' + str(numberGuessed))
else:
    print('you lost, the number to guess was ' + str(numberToGuess))
    