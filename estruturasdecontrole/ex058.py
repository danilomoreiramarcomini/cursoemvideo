import random

number = int(input('Type a number between 0 and 10:'))
random_number = random.randint(0, 10)
counter = 0

while random_number != number:
    if number > random_number:
        counter += 1
        print('Type the lower number.')
        number = int(input('Type a number between 0 and 10:'))

    elif number < random_number:
        counter += 1
        print('Type the bigger number.')
        number = int(input('Type a number between 0 and 10:'))

    else:
        number = int(input('Type a number between 0 and 10:'))
        counter += 1
print(f'Congratulations, you needed \033[34m{counter}\033[38m times.'
      f' \nYup, I think in \033[34m{random_number}')
