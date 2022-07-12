import random

tuple_empty = (random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9),
               random.randint(1, 9))
print(f"The biggest number is: {max(tuple_empty)}\nThe smallest number is: {min(tuple_empty)}")
for iteration in tuple_empty:
    print(iteration)


