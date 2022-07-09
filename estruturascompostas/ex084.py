listPeople = list()
listWeight = list()
listName = list()

while True:
    listPeople.append(str(input('Name:').title()))
    listPeople.append(float(input('Weight:')))
    choiceInput = int(input('Want continue? 1 yes or 2 No:'))
    if choiceInput != 1:
        break

for people in range(1, len(listPeople), 2):
    listWeight.append(listPeople[people])
for people in range(0, len(listPeople), 2):
    listName.append(listPeople[people])
print(f'{len(listName)} People registered')

weightMax = max(listWeight)
weightMin = min(listWeight)

print(f'{listName[listWeight.index(weightMax)]} has {weightMax}')
print(f'{listName[listWeight.index(weightMin)]} has {weightMin}')
