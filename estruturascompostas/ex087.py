import numpy

array = numpy.zeros(shape=(1, 3, 3))
listSum = list()
listSecond = list()
listThird = list()
for element in range(0, 3):
    array[0][0][element] = int(input(f'Enter with a number [0:{element}]:'))
    if array[0][0][element] % 2 == 0:
        listSum.append(array[0][0][element])
for element in range(0, 3):
    array[0][1][element] = int(input(f'Enter with a number [1:{element}]:'))
    if array[0][1][element] % 2 == 0:
        listSum.append(array[0][1][element])
        listSecond.append(array[0][1][element])
for element in range(0, 3):
    array[0][2][element] = int(input(f'Enter with a number [2:{element}]:'))
    listThird.append(array[0][2][element])
    if array[0][2][element] % 2 == 0:
        listSum.append(array[0][2][element])
for element in range(0, 3):
    print(array[0][element])

print(f'The sum between the even values is {sum(listSum)}')
print(f'the sum of the values in the third column is {sum(listThird)}')
print(f'The highest value in the second column is {max(listSecond)}')
