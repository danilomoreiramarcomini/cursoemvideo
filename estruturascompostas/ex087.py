import numpy

array = numpy.zeros(shape=(1, 3, 3))
list_sum = list()
list_second = list()
list_third = list()
for element in range(0, 3):
    array[0][0][element] = int(input(f"Enter with a number [0:{element}]: "))
    if array[0][0][element] % 2 == 0:
        list_sum.append(array[0][0][element])
for element in range(0, 3):
    array[0][1][element] = int(input(f"Enter with a number [1:{element}]: "))
    if array[0][1][element] % 2 == 0:
        list_sum.append(array[0][1][element])
        list_second.append(array[0][1][element])
for element in range(0, 3):
    array[0][2][element] = int(input(f"Enter with a number [2:{element}]: "))
    list_third.append(array[0][2][element])
    if array[0][2][element] % 2 == 0:
        list_sum.append(array[0][2][element])
for element in range(0, 3):
    print(array[0][element])

print(f"The sum between the even values is {sum(list_sum)}")
print(f"the sum of the values in the third column is {sum(list_third)}")
print(f"The highest value in the second column is {max(list_second)}")
