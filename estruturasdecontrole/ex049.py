number = int(input('Type a number:'))

for i in range(number, number * 11, number):

    print(f'\033[34m{number}\033[38m * \033[34m{i / number:.0f}\033[38m = \033[34m{i}\033[38m')
