print('Number Guessing Game')
print('Guess a Number between 1 to 9')

import random
number =  random.randint(1,9)
print(number)
chances = 0
guess = int(input('Enter your guess : '))

while number != "guess":
    print
    if (guess < number):
        print ("guess is low")
        chances=+1
        guess = int(input("Enter an integer from 1 to 9: "))
    elif (guess > number):
        print ("guess is high")
        chances=+1
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print ("you guessed it!")
        break
    