while True:
    mult_table = int(input('Type a number:'))
    if mult_table < 0:
        break
    for number in range(1, 11):
        print(f'{mult_table} * {number} = {mult_table * number}')
