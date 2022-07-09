first_term = int(input('Type the first term:'))
reason = int(input('Type the reason:'))
term = first_term
sequence = 1
while sequence <= 10:
    print(f'{term}')
    sequence += 1
    term += reason
