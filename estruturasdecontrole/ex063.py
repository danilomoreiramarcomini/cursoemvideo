term = int(input("Terms: "))
counter = 0
first_support = 0
second_support = 1
print(f"{first_support}\n{second_support}")
while counter != term:

    fibonacci = first_support + second_support
    first_support = second_support
    second_support = fibonacci
    counter += 1
    print(fibonacci)
