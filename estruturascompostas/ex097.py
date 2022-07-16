def write(text):
    support = len(text)
    print(f"-" * support)
    print(f"{text.center(0)}")
    print(f"-" * support)


write(str(input("Write your text here: ")).title())
