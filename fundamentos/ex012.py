product_price = float(input("Product price: "))
print(f"\033[38mNew price $:\033[34m{(product_price + (0.05 * product_price)):.2f}")

