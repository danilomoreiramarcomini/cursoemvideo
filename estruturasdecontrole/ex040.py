import statistics

first_note = float(input('Type the first note:'))
second_note = float(input('Type the second note:'))

average = statistics.fmean([first_note, second_note])

if average < 5:
    print(f'Disapproved\nYour average was\033[34m {average:.2f}')
elif 5 <= average <= 6.9:
    print(f'Recuperação\nYour average was\033[34m {average:.2f}')
else:
    print(f'Aprovado\nYour average was\033[34m {average:.2f}')
