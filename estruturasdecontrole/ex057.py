gender = str(input("Type your gender: ")).upper()[0]

if gender != "M" or gender != "F":
    while gender != "F" and gender != "M":
        print("Choice between M or F")
        gender = str(input("Type your gender: ")).upper()[0]

if gender == "M" or gender == "F":
    print("Gender registred!")
