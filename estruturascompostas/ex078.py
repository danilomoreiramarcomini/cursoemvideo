listPython = list()

for value in range(0, 5):
    valueInput = int(input('Enter with a number:'))
    listPython.append(valueInput)

bigger = max(listPython)
lower = min(listPython)

print(f'The highest number is {bigger} on {listPython.index(bigger)}ªth position \nThe smallest number is {lower} on '
      f'{listPython.index(lower)}ªth position')
