listPython = list()
while True:
    numberInput = int(input('Enter with a number:'))
    if numberInput in listPython:
        print(f'There is {numberInput} in list')
    if numberInput not in listPython:
        listPython.append(numberInput)
    choice = int(input('Want continue: [1] Yes [2] No\nChoice:'))
    if choice != 1:
        break

print(f'{sorted(listPython)}')
