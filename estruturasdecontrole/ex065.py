import statistics

numbers = []
number = int(input('Type a number:'))
numbers.append(number)
counter = 0
choice = str
while choice != 'N':
    choice = input('continue? Type N to No or Y to Yes:').upper()
    if choice == 'Y':
        number = int(input('Type a number:'))
        numbers.append(number)
    counter += 1
print(f'The average {statistics.median(numbers)}\nThe bigger value typed has {max(numbers)}\n'
      f'The lower value typed has {min(numbers)}\nYou typed {counter} numbers')
