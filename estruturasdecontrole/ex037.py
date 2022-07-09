number = int(input('Type a decimal number:'))
choice = int(input('[1] Binary [2] Octal [3] Hexadecimal:'))

if choice == 1:
    binary = str(bin(number))
    print(f'\033[34m{binary[2:]}')
elif choice == 2:
    octal = str(oct(number)).upper()
    print(f'\033[34m{octal[2:]}')
elif choice == 3:
    hexadecimal = str(hex(number)).upper()
    print(f'\033[34m{hexadecimal[2:]}')

else:
    print('Choose one of the options')
