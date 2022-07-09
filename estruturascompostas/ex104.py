def my_number():
    """" This function read a number and returns a message of erro if this number not was of type numeric
    :return: A message of erro and a new input, or the number typed
    """
    while True:
        number_str = str(input('Number:'))
        if number_str.isnumeric():
            print(f'Your typed {number_str}')
            break
        else:
            print('\033[31mError\033[38m')


my_number()
