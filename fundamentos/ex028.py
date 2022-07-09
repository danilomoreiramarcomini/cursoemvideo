import random

number = int(input("Number: "))
number_by_computer = random.randint(0, 5)

if number == number_by_computer:
    print(f"You win, I think in number {number_by_computer}")
else:
    print(f"You lose, I think in number {number_by_computer}")
