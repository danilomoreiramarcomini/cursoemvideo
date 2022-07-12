list_people = list()
list_weight = list()
list_name = list()

while True:
    list_people.append(str(input("Name: ").title()))
    list_people.append(float(input("Weight: ")))
    choice_input = int(input("Want continue? 1 yes or 2 No: "))
    if choice_input != 1:
        break

for people in range(1, len(list_people), 2):
    list_weight.append(list_people[people])
for people in range(0, len(list_people), 2):
    list_name.append(list_people[people])
print(f"{len(list_name)} People registered")

weight_max = max(list_weight)
weight_min = min(list_weight)

print(f"{list_name[list_weight.index(weight_max)]} has {weight_max}")
print(f"{list_name[list_weight.index(weight_min)]} has {weight_min}")
