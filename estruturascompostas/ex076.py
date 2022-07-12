products_and_prices = ("Milk", 10.50, "Beans", 10.45, "Rice", 15.70, "Coffee", 12.50)

for iteration in range(0, len(products_and_prices)):
    if iteration % 2 == 0:
        print(f"{products_and_prices[iteration]:.<20}$:{products_and_prices[iteration + 1]:.2f}")
