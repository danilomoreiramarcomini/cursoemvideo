import datetime

informations = dict()

informations["name"] = str(input('Name: ')).title()
informations["Year of birth"] = int(input("Year of birth: "))
informations["CTPS"] = int(input("CTPS: "))
age_calc = datetime.datetime.now()
informations["Age"] = current_age = age_calc.year - informations['Year of birth']

if informations["CTPS"] == 0:
    for key, value in informations.items():
        print(f"{key}: {value}")

elif informations["CTPS"] != 0:
    while True:
        gender = str(input("Gender: ").title())
        if gender == "M":
            years = int(35)
            break
        elif gender == "F":
            years = int(30)
            break

    informations["Retirement"] = str(f"{informations['Age'] + years} year")
    informations["Year of Hire"] = int(input("Year of hire: "))
    informations["Salary"] = float(input("Salary: "))

    for key, value in informations.items():
        print(f"{key}: {value}")
