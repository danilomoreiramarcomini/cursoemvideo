import random

tupleEmpty = (random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9),
              random.randint(1, 9))
print(f'The biggest number is: {max(tupleEmpty)}\nThe smallest number is:{min(tupleEmpty)}')
for iteration in tupleEmpty:
    print(iteration)


