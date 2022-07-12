import random

from time import sleep

amount_of_bets_input = int(input("Amounts of bets: "))
list_bets = list()
list_support = list()

while True:
    for number in range(0, 6):
        value_support = random.randint(1, 60)
        while value_support in list_support:
            value_support = random.randint(1, 60)
        if value_support not in list_support:
            list_support.append(value_support)

    copy_support = list_support.copy()
    list_bets.append(copy_support)
    list_support.clear()
    if len(list_bets) == amount_of_bets_input:
        break

for element in range(0, len(list_bets)):
    print(f"The {element + 1}º numbers: {sorted(list_bets[element])}")
    sleep(1)

