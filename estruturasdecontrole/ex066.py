numbers = []
counter = 0
while True:
    number = int(input('Type the number lower 999 or 999 for quit:'))
    if number == 999:
        break
    counter += 1
    numbers.append(number)

print(f'You typed {counter} times.\nThe sum between values typed is {sum(numbers)}')
