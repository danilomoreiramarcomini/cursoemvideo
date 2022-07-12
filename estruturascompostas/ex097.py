def write(text):
    support = len(text)
    print(f"-" * support)
    print(f"{text.center(0)}")
    print(f"-" * support)


text_input = str(input("Write your text here: ")).title()
write(text_input)
