list_python = list()
while True:
    number_input = int(input("Enter with a number: "))
    list_python.append(number_input)
    choice_input = int(input("Want continue [1 Yes  2 No]: "))
    if choice_input != 1:
        break

if 5 in list_python:
    boolean = True
else:
    boolean = False

print(f"You wrote {len(list_python)} values\nThe list in order {sorted(list_python, key=None, reverse=True)}"
      f"\nThere is 5 on list? {boolean}")
