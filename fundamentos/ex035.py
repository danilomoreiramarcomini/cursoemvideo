side_a = int(input("Side a: "))
side_b = int(input("Side b: "))
side_c = int(input("Side c: "))

if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
    print("Triangule")
else:
    print("Not triangule")
