import random

jokenpo = ["Stone", "Paper", "Scissors"]

choice_user = str(input("Choice between 1, 2 or 3"
                        "\n[1] Stone   [2] Paper   [3] Scissors: ")).title()

choice_machine = random.choice(jokenpo)

if choice_user == "Stone" or choice_user == "1":
    if choice_machine == "Paper":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you losed!")
    elif choice_machine == "Scissors":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you wined")
    elif choice_machine == 'Stone':
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you tied!")

elif choice_user == "Paper" or choice_user == "2":
    if choice_machine == "Paper":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you tied!")
    elif choice_machine == "Scissors":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you losed!")
    elif choice_machine == "Stone":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you wined!")

elif choice_user == "Scissors" or choice_user == "3":
    if choice_machine == "Paper":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you wined!")
    elif choice_machine == "Scissors":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you tied!")
    elif choice_machine == "Stone":
        print(f"Machine choice \033[34m{choice_machine}\033[38m, you losed!")
else:
    print("\033[31mMake a correct choice!")
