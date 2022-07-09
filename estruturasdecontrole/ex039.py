from time import localtime

gender = str(input('Choice your gender. Choice between Male or Female:')).title()

if gender == 'Male':
    birth_date = int(input('Type the year of your birth:'))

    date = localtime()
    year = date.tm_year

    majority = int(year - birth_date)
    year_of_enlistment = birth_date + 17

    if majority > 18:
        print(f'You have \033[34m{majority}\033[38m year old, his year of enlistment was in \033[34m'
              f'{year_of_enlistment}')
    elif majority == 18:
        print(f'You have \033[34m{year - birth_date}\033[38m'
              f' Welcome to the army')
    elif majority <= 17:
        print(f'You have \033[34m{year - birth_date}\033[38m year old'
              f'.\nYour enlistment will be in \033[34m{year_of_enlistment}\033[38m Ainda falta \033[34m'
              f'{year_of_enlistment - (year - majority)}\033[38m year old')

elif gender == 'Female':
    print('Only men are required to enlist!')

elif gender != 'Male' or gender != 'Female':
    print('???')
