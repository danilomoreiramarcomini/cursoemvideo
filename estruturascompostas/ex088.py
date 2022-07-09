import random

from time import sleep

amountOfBetsInput = int(input('Amounts of bets:'))
listBets = list()
listSupport = list()

while True:
    for number in range(0, 6):
        valueSupport = random.randint(1, 60)
        while valueSupport in listSupport:
            valueSupport = random.randint(1, 60)
        if valueSupport not in listSupport:
            listSupport.append(valueSupport)

    copySupport = listSupport.copy()
    listBets.append(copySupport)
    listSupport.clear()
    if len(listBets) == amountOfBetsInput:
        break

for element in range(0, len(listBets)):
    print(f'The {element + 1}º numbers: {sorted(listBets[element])}')
    sleep(1)

