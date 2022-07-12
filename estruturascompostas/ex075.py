tuple_empty = (int(input("Enter with a number: ")), int(input("Enter with a number: ")),
               int(input("Enter with a number: ")), int(input("Enter with a number: ")),)
print(f"The number 9 appears {tuple_empty.count(9)} times")
if 3 in tuple_empty:
    print(f"The number 3 is in position {tuple_empty.index(3) + 1}ºth")
else:
    x = 0
print(f"The number even: ")
for iteration in range(0, len(tuple_empty)):
    if tuple_empty[iteration] % 2 == 0:
        print(f'{tuple_empty[iteration]}', end=' ')
