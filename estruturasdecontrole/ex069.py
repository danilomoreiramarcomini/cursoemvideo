adults = 0
mans = 0
womans = 0
while True:
    age = int(input('Age:'))
    gender = ' '
    while gender != 'M' and gender != 'F':
        gender = str(input('gender:')).strip().upper()[0]
    if age > 18:
        adults += 1
    if gender == 'M':
        mans += 1
    if gender == 'F' and age < 20:
        womans += 1
    support = ' '
    while support != 'Y' and support != 'N':
        support = str(input('Continue? ')).strip().upper()[0]
    if support == 'N':
        break

print(f'We have {adults} adults, {womans} womans with lower of 20 years and {mans} mans')
