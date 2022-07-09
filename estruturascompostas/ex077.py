tupleLetters = ('Python', 'Ruby', 'JavaScript', 'PHP', 'Java')

for iteration in range(0, len(tupleLetters)):
    support = tupleLetters.index(tupleLetters[iteration])
    letter = tupleLetters[support].casefold()
    for i in range(0, len(letter)):
        if letter[i] in 'aeiou':
            print(f'{tupleLetters[iteration]}: {letter[i]}')
