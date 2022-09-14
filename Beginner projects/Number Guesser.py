import random

ans = random.randrange(1,100)
guess = int(input('Guess a number within the range of 1 - 100\n'))
LowerLimit = 1
UpperLimit = 100

while guess != ans:
    if guess > ans:
        print('Your guess is too high!')
        UpperLimit = guess
        guess = int(input('Guess a new number within the range of ' + str(LowerLimit) + ' and ' + str(guess) + '\n'))
    else:
        print('Your guess is too low!')
        LowerLimit = guess
        guess = int(input('Guess a new number within the range of ' + str(guess) + ' and ' + str(UpperLimit) + '\n'))
else:
    print('You Guessed the correct number of ' + str(ans) )
