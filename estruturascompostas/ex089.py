list_average = list()
list_notes = list()
list_names = list()
list_support_notes = list()

while True:
    list_names.append(str(input("Enter with name of student: ").title()))
    list_support_notes.append(float(input("Enter with the first note: ")))
    list_support_notes.append(float(input("Enter with the second note: ")))
    list_average.append((list_support_notes[0] + list_support_notes[1]) / 2)
    choiceInput = int(input("Do you want continue? 1 Yes or 2 No: "))

    copyNo = list_support_notes.copy()
    list_notes.append(copyNo)
    list_support_notes.clear()
    if choiceInput != 1:
        break

print(f"{'Nº.':<5}{'NAME':<10}'{'AVERAGE':>8}")
print("-" * 30)
for element in range(0, (len(list_names))):
    print(f"{element:<5}   {list_names[element]:<10}  {list_average[element]:>8}")

while True:
    show_note_input = int(input("Show notes of student? [999 - quit]: "))
    if show_note_input == 999:
        break
    else:
        print(f"{list_notes[show_note_input]}")
