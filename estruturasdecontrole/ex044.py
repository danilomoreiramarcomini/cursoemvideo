value = float(input("Enter the amount to be paid $: "))

choice = int(input("Choice the form of payment\n[1] Money or check\n[2] Card\n"
                   "[3] 2x in card\n[4] 3x in card\n"))
if choice == 1:
    value = value - (value * 0.1)
    print(f"$: \033[34m{value}")
elif choice == 2:
    value = value - (value * 0.5)
    print(f"$: \033[34m{value}")
elif choice == 3:
    value = value / 2
    print(f"You will pay twice $: \033[34m{value:.2f}")
elif choice == 4:
    number_of_installments = int(input("Enter how many times you will pay: "))
    value = value + (value * 0.2)
    print(f"You will pay $: \033[34m{value / number_of_installments}\033[38m in \033[34m{number_of_installments}"
          f" \033[38mtimes")

else:
    print("\033[31mERROR")
