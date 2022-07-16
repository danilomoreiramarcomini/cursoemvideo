def area(width, length):
    print(f"Size \033[34m{width*length:.1f}\033[38m m²")


area(float(input("Width: ")), float(input("Length: ")))
