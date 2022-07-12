list_python = list()
list_evens = list()
list_odds = list()

while True:
    number_input = int(input("Enter with a number: "))
    list_python.append(number_input)
    choice_input = int(input("Want continue [1 Yes or 2 No]: "))
    if choice_input != 1:
        break

for item in range(0, len(list_python)):
    if list_python[item] % 2 == 0:
        list_evens.append(list_python[item])

    else:
        list_odds.append(list_python[item])

print(f"Numbers wrote:{list_python}\nNumbers Odds:{list_odds}\nNumbers Evens:{list_evens}")
