width = float(input("Width: "))
height = float(input("Height: "))
area = width * height
area_painted = area / 2
print(f"\033[38myou need: \033[34m{area_painted:.0f}\033[38m liters of ink")
