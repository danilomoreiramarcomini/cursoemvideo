def counter():
    for element in range(1, 11, 1):
        print(f'{element}', end=' ')
    print('\n-----------------------')

    for element in range(10, -1, -2):
        print(f'{element}', end=' ')
    print('\n-----------------------')

    start = int(input('Star:'))
    end = int(input('End:'))
    step = int(input('Step:'))

    if step < 0:
        step = abs(step)
    if step == 0:
        step = 1

    if end > start:
        for number in range(start, end + 1, step):
            print(f'{number}', end=' ')
    else:
        for number in range(start, end - 1, step - (step * 2)):
            print(f'{number}', end=' ')


counter()
