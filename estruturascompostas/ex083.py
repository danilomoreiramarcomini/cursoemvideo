listPython = list()
expressionInput = str(input('Enter with the math expression:'))
listPython.append(expressionInput)
listPython.append('')
left = listPython[0].count('(')
right = listPython[0].count(')')

print('Valid') if left == right else print('Invalid')
