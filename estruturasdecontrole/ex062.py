first_term = int(input("Type the first term: "))
reason = int(input("Type the reason: "))
term = first_term
sequence = 1
terms = 0
new_term = 10
while new_term != 0:
    terms = terms + new_term
    while sequence <= terms:
        print(f'{term}')
        sequence += 1
        term += reason

    new_term = int(input("Continue with amount terms: "))
