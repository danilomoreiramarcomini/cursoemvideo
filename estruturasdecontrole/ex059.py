choice = int(input("=====CALCULATOR=====\n[1] - MULTIPLICATION\n[2] - DIVISION\n[3] - ADITION\n[4] - "
                   "SUBTRACTION\n[5] - FINISH\nCHOICE A OPTION: "))

while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
    choice = int(input("=====CALCULATOR=====\n[1] - MULTIPLICATION\n[2] - DIVISION\n[3] - ADITION\n[4] - "
                       "SUBTRACTION \nCHOICE A OPTION: "))

if choice == 1:
    print("=====MULTIPLICATION=====\n")
    multiplying = float(input("Type the first number: "))
    multiplier = float(input("Type the second number: "))
    print(f"The result is {multiplying * multiplier}")

if choice == 2:
    print("=====DIVISION=====\n")
    dividend = float(input("Type the first number: "))
    divider = float(input("Type the second number: "))
    print(f"The result is {dividend / divider}")

if choice == 3:
    print("=====ADITION=====\n")
    first_installment = float(input("Type the first number: "))
    second_installment = float(input("Type the second number: "))
    print(f"The result is {first_installment + second_installment}")

if choice == 4:
    print("=====SUBTRACTION=====\n")
    minuendo = float(input("Type the first number: "))
    subtrahend = float(input("Type the second number: "))
    print(f"The result is {minuendo - subtrahend}")

if choice == 5:
    print("The end")
