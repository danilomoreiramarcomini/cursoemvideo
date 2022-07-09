weight = []

for people in range(1, 6):
    value_weight = float(input(f'Type the weight of {people}°:'))
    weight.append(value_weight)
print(f'The bigger weight \033[35m{max(weight)}\033[38m kilogram. The lower weight \033[35m{min(weight)}'
      f'\033[38m kilogram')
