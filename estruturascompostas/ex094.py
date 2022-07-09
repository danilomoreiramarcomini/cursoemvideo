information_peoples = dict()
new_people = int(1)
ages = list()
women_name = list()
above_average_ages = list()
while True:

    name = information_peoples[f'{new_people}º Name'] = str(input('Name:')).title()
    while True:
        gender = information_peoples[f'{new_people}º Gender'] = str(input('Gender:')).upper()[0]
        if gender in 'MF':
            break
    age = information_peoples[f'{new_people}º Age'] = int(input('Age:'))
    while True:
        continue_choice = str(input('You want continue:')).upper()[0]
        if continue_choice in 'YN':
            break
    ages.append(age)
    if gender == 'F':
        women_name.append(name)
    new_people += 1
    if continue_choice == 'N':
        average = float((sum(ages) / len(ages)))
        if age > average:
            above_average_ages.append(age)
        print(f'_' * 30)
        print(f'Number of people regitered: {new_people - 1}')
        print(f'_' * 30)
        print(f'Average age: {average:.2f} age')
        print(f'_' * 30)
        print(f'Women:')
        for woman in women_name:
            print(f'{woman}')
        print(f'_' * 30)
        print(f'Above Average Age:')
        for above_average_age in above_average_ages:
            print(f'{above_average_age}')
        print(f'_' * 30)
        break
