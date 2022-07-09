kilometer = float(input("Kilometers: "))

if kilometer > 80:
    print(f"Pay $:{(kilometer - 80) * 7:.2f}")
else:
    print(f"Good trip")
