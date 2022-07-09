kilometers = float(input("kilometers: "))

if kilometers > 200:
    print(f"Pay $:{kilometers * 0.50:.2f}")
else:
    print(f"Pay $:{kilometers * 0.45:.2f}")

