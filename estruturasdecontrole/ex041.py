from time import localtime

year_of_birth = int(input('Type your date of birth:'))

date = localtime()
year_of_system = date.tm_year
athlete_s_age = year_of_system - year_of_birth

if athlete_s_age <= 9:
    print(f'You have \033[34m{athlete_s_age}\033[38m years old. Little')
elif 9 < athlete_s_age <= 14:
    print(f'You have \033[34m{athlete_s_age}\033[38m years old. Childish')
elif 14 < athlete_s_age <= 19:
    print(f'You have \033[34m{athlete_s_age}\033[38m years old. Junior')
elif 19 < athlete_s_age <= 25:
    print(f'You have \033[34m{athlete_s_age}\033[38m years old. Senior')
elif athlete_s_age > 25:
    print(f'You have \033[34m{athlete_s_age}\033[38m years old. Master')
