first_number = float(input("Type the first number: "))
second_number = float(input("Type the second number: "))

if first_number > second_number:
    print(f"\033[34m{first_number:.1f}\033[38m is bigger than \033[34m{second_number:.1f}")
elif second_number > first_number:
    print(f"\033[34m{second_number:.1f}\033[38m is bigger than \033[34m{first_number:.1f}")
elif first_number == second_number:
    print("The dictionary is equals")
else:
    print("Type correctly")
