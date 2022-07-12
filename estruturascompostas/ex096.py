def square_area(width, length):
    print(f"Size \033[34m{width*length:.2f}\033[38mm²")


width_size = float(input("Width: "))
length_size = float(input("Length: "))
square_area(width_size, length_size)
