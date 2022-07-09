listAverage = list()
listNotes = list()
listNames = list()
listSupportNotes = list()

while True:
    listNames.append(str(input('Enter with name of student:').title()))
    listSupportNotes.append(float(input('Enter with the first note:')))
    listSupportNotes.append(float(input('Enter with the second note:')))
    listAverage.append((listSupportNotes[0] + listSupportNotes[1]) / 2)
    choiceInput = int(input('Do you want continue? 1 Yes or 2 No:'))

    copyNo = listSupportNotes.copy()
    listNotes.append(copyNo)
    listSupportNotes.clear()
    if choiceInput != 1:
        break

print(f'{"Nº.":<5}{"NAME":<10}"{"AVERAGE":>8}')
print('-' * 30)
for element in range(0, (len(listNames))):
    print(f'{element:<5}   {listNames[element]:<10}  {listAverage[element]:>8}')

while True:
    showNoteInput = int(input('Show notes of student? [999 - quit]: '))
    if showNoteInput == 999:
        break
    else:
        print(f'{listNotes[showNoteInput]}')
