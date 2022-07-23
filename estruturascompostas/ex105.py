def notes():
    """
     This function reads n notes and adds all data inside the dictionary and notes inside the list.
    After the function calculates the note maximum, minimum, and average between notes.
    For last the function ask about showing or note your situation.
    :return: All notes, Maximum note, Minimum note, average between the note and your situation or not
    """
    amount_notes = int(input("How many notes do you want to add: "))
    list_notes = list()
    dictonary_notes = dict()

    for note in range(1, amount_notes + 1):
        note_input = float(input(f"{note}º note: "))
        list_notes.append(note_input)
        dictonary_notes[f"{note}º note"] = note_input

    average_note = sum(list_notes) / amount_notes

    dictonary_notes["Maximum note"] = max(list_notes)
    dictonary_notes["Minimum note"] = min(list_notes)
    dictonary_notes["Average note"] = average_note

    if average_note < 5:
        dictonary_notes["Situation"] = "Bad"
    if 5 <= average_note <= 8:
        dictonary_notes["Situation"] = "Good"
    if average_note > 8:
        dictonary_notes["Situation"] = "Excellent"
    while True:
        situation = str(input("Do you want show your situation: [Y/n]: ")).title()
        if "N" in situation:
            del dictonary_notes["Situation"]
            print(dictonary_notes)
            break
        if "Y" in situation:
            print(dictonary_notes)
            break


notes()
