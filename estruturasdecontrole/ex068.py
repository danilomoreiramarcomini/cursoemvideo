import random

counter = 0
while True:
    computer = random.randint(0, 10)
    user = int(input('Type a number:'))
    choice = str(input('Type O for odd or E for even:')).upper()[0]
    result = (computer + user)
    if choice == 'O':
        if result % 2 == 0:
            print(f'You win! The computer choiced {computer}')
            counter += 1

        else:
            print(f'You lose! HA-HA-HA-HA\nThe computer choiced {computer}, you win {counter} times')
            break
    if choice == 'E':
        if result % 2 != 0:
            print(f'You win! The computer choiced {computer}')
            counter += 1

        else:
            print(f'You lose! HA-HA-HA-HA\nThe computer choiced {computer}, you win {counter} times')
            break
