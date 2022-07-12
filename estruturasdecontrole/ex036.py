house_value = float(input("Value of house: "))
salary = float(input("Salary: "))
installment_time = int(input("In how many years do you intend to pay: "))
months_to_years_conversion = int(installment_time * 12)
installment = float(house_value / months_to_years_conversion)
thirty_percent = (salary * 0.30)

if installment > thirty_percent:
    print(f"\033[34mLoan denied\033[38m!")
else:
    print(f"\033[34mApproved loan\033[38m!")
