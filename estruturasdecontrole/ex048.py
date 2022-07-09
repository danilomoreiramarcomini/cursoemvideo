counter = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        counter += i
print(f'\033[34m{counter}')
