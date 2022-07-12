list_python = list()

for value in range(0, 5):
    valueInput = int(input("Enter with a number: "))
    list_python.append(valueInput)

bigger = max(list_python)
lower = min(list_python)

print(f"The highest number is {bigger} on {list_python.index(bigger)}ªth position \nThe smallest number is {lower} on "
      f"{list_python.index(lower)}ªth position")
