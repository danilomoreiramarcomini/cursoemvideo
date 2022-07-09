listPython = list()
while True:
    numberInput = int(input('Enter with a number:'))
    listPython.append(numberInput)
    choiceInput = int(input('Want continue [1 Yes  2 No]:'))
    if choiceInput != 1:
        break

if 5 in listPython:
    boolean = True
else:
    boolean = False

print(f'You wrote {len(listPython)} values\nThe list in order {sorted(listPython, key=None, reverse=True)}'
      f'\nThere is 5 on list? {boolean}')
