import random

number_of_rolls = int(input('How many rolls do you want?\n'))
res = []

for i in range(number_of_rolls):
    res.append(random.randint(1,6))

print('Your rolls are ' + str(res))