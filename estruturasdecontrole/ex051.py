init = int(input('Init:'))
counter = int(input('Counter:'))
tenth_term = init + (10 - 1) * counter

for i in range(init, tenth_term + counter, counter):
    print(f'\033[34m{i}\n')

print('Finished')
