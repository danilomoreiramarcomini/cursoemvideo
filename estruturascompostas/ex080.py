listPython = list()
newListPython = list()
counter = 0
for number in range(0, 5):
    numberInput = int(input('Enter with a number:'))
    listPython.append(numberInput)

for value in range(0, 5):
    support = min(listPython)
    newListPython.insert(counter, support)
    listPython.pop(listPython.index(support))
    counter += 1

listPython = newListPython.copy()
newListPython.clear()
print(listPython)
