values = []
products = []
amount_products = 0
while True:
    product = str(input('Product:')).title()
    value = float(input('Value $:'))
    choice = ' '
    while choice not in 'Y' and choice not in 'N':
        choice = str(input('Continue:')).upper()[0]

    if value >= 1000:
        amount_products += 1
    products.append(product)
    values.append(value)
    the_min = min(values)
    the_max = max(values)
    the_sum = sum(values)
    the_min_position = values.index(min(values))
    if choice == 'N':
        print(f"the total has $:{the_sum:.2f}\n{products[the_min_position]} it's the cheapest item, your number is $:"
              f"{values[the_min_position]:.2f}\n'There is {amount_products} "
              f"products bigger that $:1000.00")
        break
