import random

students = list()
students.append(str(input("First name: ")).title())
students.append(str(input("Second name: ")).title())
students.append(str(input("Third name: ")).title())
students.append(str(input("Fourth name: ")).title())

print(random.choice(students))
