tupleEmpty = (int(input('Enter with a number:')), int(input('Enter with a number:')),
              int(input('Enter with a number:')), int(input('Enter with a number:')),)
print(f'The number 9 appears {tupleEmpty.count(9)} times')
if 3 in tupleEmpty:
    print(f'The number 3 is in position {tupleEmpty.index(3) + 1}ºth')
else:
    x = 0
print(f'The number even: ')
for iteration in range(0, len(tupleEmpty)):
    if tupleEmpty[iteration] % 2 == 0:
        print(f'{tupleEmpty[iteration]}', end=' ')
