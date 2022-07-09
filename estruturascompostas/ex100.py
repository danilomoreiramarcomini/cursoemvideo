import random

my_list = list()
new_list = list()


def numbers_generator():
    for value in range(0, 5):
        my_list.append(random.randint(0, 100))

    for value in my_list:
        print(f'{value}', end=" ")


def numbers_generated(parameter_list):
    for value in my_list:
        if value % 2 == 0:
            parameter_list.append(value)
    print(f'\nThe sum between the numbers evens is equal {sum(parameter_list)}')


numbers_generator()
numbers_generated(new_list)
