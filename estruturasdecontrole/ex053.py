palindrome = str(input('Type a phrase:')).replace(' ', '').title()
support = (palindrome[::-1])

if palindrome == support:
    print(f'\033[34m{palindrome}\033[38m palindrome')
else:
    print(f'\033[34m{support}\033[38m no palindrome')
