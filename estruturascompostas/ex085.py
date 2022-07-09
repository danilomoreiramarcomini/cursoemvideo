numbersList = [[], []]
while True:
    numberInput = int(input('Enter with a number:'))
    choiceInput = int(input('Do you want continue? 1 Yes or 2 No:'))
    if numberInput % 2 == 0:
        numbersList[0].append(numberInput)
    else:
        numbersList[1].append(numberInput)

    if choiceInput != 1:
        break
print('EVENS')
numbersList[0].sort()
for even in numbersList[0]:
    print(f'{even}', end=' ')
print('\nODDS')
numbersList[1].sort()
for odd in numbersList[1]:
    print(f'{odd}', end=' ')
