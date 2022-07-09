salary = float(input("Salary: "))

if salary > 1250:
    print(f"New salary $:{((salary * 0.10) + salary):.2f}")
else:
    print(f"New salary $:{((salary * 0.15) + salary):.2f}")
