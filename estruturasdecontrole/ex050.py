counter = 0

for i in range(0, 6):
    number = int(input("Type a number: "))
    if number % 2 == 0:
        counter += number
if counter % 2 == 0:
    print(f"The sum between the numbers eves are \033[34m{counter}")
