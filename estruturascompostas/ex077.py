tuple_letters = ("Python", "Ruby", "JavaScript", "PHP", "Java")

for iteration in range(0, len(tuple_letters)):
    support = tuple_letters.index(tuple_letters[iteration])
    letter = tuple_letters[support].casefold()
    for i in range(0, len(letter)):
        if letter[i] in "aeiou":
            print(f"{tuple_letters[iteration]}: {letter[i]}")
