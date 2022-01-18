import random

number=(random.randint(1,9))

chances=0

print("Guess a number between 1 to 9")

while chances < 5:

    guess = int(input('Enter your guess: '))

    if guess == number :
        print ("Congo You Won")
        break

    elif guess < number:
        print('Your Guess Was Low,Guess A Higher Number',guess)

    else :
        print('Your Guess Was Higher,Guess A Low Number',guess)

    chances+=1

    if not chances < 5:
        print('You Lost The Number Was',number)