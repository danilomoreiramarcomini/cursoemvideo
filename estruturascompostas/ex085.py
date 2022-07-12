numbers_list = [[], []]
while True:
    number_input = int(input("Enter with a number: "))
    choice_input = int(input("Do you want continue? 1 Yes or 2 No: "))
    if number_input % 2 == 0:
        numbers_list[0].append(number_input)
    else:
        numbers_list[1].append(number_input)

    if choice_input != 1:
        break
print("EVENS")
numbers_list[0].sort()
for even in numbers_list[0]:
    print(f"{even}", end=" ")
print("\nODDS")
numbers_list[1].sort()
for odd in numbers_list[1]:
    print(f"{odd}", end=" ")
