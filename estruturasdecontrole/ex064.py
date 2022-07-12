total = []
number = int(input("Type 999 for finish | Type a number: "))
total.append(number)
sum_between_numbers = int(0)
counter = 0
while number != 999:
    number = int(input("Type 999 for finish | Type a number: "))
    total.append(number)
    sum_between_numbers = sum(total)
    counter += 1
print(f"The sum between all values is {sum_between_numbers - 999}. You typed {counter} numbers")
