side_a = float(input("Type the first number: "))
side_b = float(input("Type the first number: "))
side_c = float(input("Type the first number: "))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    if side_a != side_b and side_a != side_c:
        print("\033[34mScalene")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        if side_a == side_b and side_b == side_c:
            print("\033[34mEquilateral")
        else:
            print("\033[34mIsosceles")
    elif side_a == side_b and side_b == side_c:
        print("\033[34mEquilateral")
else:
    print("\nIt's not a triangle")
