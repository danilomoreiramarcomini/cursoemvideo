list_python = list()
new_list_python = list()
counter = 0
for number in range(0, 5):
    number_input = int(input("Enter with a number: "))
    list_python.append(number_input)

for value in range(0, 5):
    support = min(list_python)
    new_list_python.insert(counter, support)
    list_python.pop(list_python.index(support))
    counter += 1

list_python = new_list_python.copy()
new_list_python.clear()
print(list_python)
