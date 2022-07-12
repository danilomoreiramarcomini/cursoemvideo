import numpy

array = numpy.zeros(shape=(1, 3, 3))

for element in range(0, 3):
    array[0][0][element] = int(input(f"Enter with a number: [0:{element}]"))
for element in range(0, 3):
    array[0][1][element] = int(input(f"Enter with a number: [1:{element}]"))
for element in range(0, 3):
    array[0][2][element] = int(input(f"Enter with a number: [2:{element}]"))
for element in range(0, 3):
    print(array[0][element])
