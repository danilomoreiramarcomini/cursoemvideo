phrase = str(input("Phrase: ")).lower()
phrase_list = phrase.split()
print(phrase_list)
print(f"{phrase.count('a')}")
print(f"{phrase.find('a') + 1}")
print(f"{phrase.rfind('a') + 1}")