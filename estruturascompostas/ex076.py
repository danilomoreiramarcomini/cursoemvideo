productsAndPrices = ('Milk', 10.50, 'Beans', 10.45, 'Rice', 15.70, 'Coffee', 12.50)

for iteration in range(0, len(productsAndPrices)):
    if iteration % 2 == 0:
        print(f'{productsAndPrices[iteration]:.<20}$:{productsAndPrices[iteration + 1]:.2f}')
