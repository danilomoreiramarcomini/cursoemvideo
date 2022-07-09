import math

opposite_side = float(input("Opposite side: "))
adjacent_side = float(input("Adjacent side: "))
print(f"\033[34m{math.sqrt((pow(adjacent_side, 2) + pow(opposite_side, 2)))}\033[38m")