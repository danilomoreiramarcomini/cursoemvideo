listPython = list()
listEvens = list()
listOdds = list()

while True:
    numberInput = int(input('Enter with a number:'))
    listPython.append(numberInput)
    choiceInput = int(input('Want continue [1 Yes or 2 No]:'))
    if choiceInput != 1:
        break

for item in range(0, len(listPython)):
    if listPython[item] % 2 == 0:
        listEvens.append(listPython[item])

    else:
        listOdds.append(listPython[item])


print(f'Numbers wrote:{listPython}\nNumbers Odds:{listOdds}\nNumbers Evens:{listEvens}')
