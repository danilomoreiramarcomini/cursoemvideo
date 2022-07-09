from datetime import datetime

largers_of_age = 0
minors_of_age = 0
for people in range(1, 8):
    year = int(input(f'Year of birth {people}°:'))
    year_current = int(datetime.today().year)
    age = year_current - year
    if age >= 18:
        largers_of_age += 1
    else:
        minors_of_age += 1

print(f'For the case, we have \033[34m{largers_of_age}\033[38m adults and \033[34m{minors_of_age}\033[38m '
      f'youngs')
