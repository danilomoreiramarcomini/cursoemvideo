list_python = list()
while True:
    number_input = int(input("Enter with a number: "))
    if number_input in list_python:
        print(f"There is {number_input} in list")
    if number_input not in list_python:
        list_python.append(number_input)
    choice = int(input("Want continue: [1] Yes [2] No\nChoice: "))
    if choice != 1:
        break

print(f"{sorted(list_python)}")
