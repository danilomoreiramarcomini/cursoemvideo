number = int(input('Type a number:'))
total = 0
for i in range(1, number + 1):
    if number % i == 0:
        print(f'\033[34m', end=' ')
        total += 1
    else:
        print('\033[34m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[38m Number \033[34m{number}\033[38m was divided\033[34m{total}\033[38m times')
if total == 2:
    print('Prime')
else:
    print('No prime')
