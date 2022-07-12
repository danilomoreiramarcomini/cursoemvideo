list_python = list()
expression_input = str(input("Enter with the math expression: "))
list_python.append(expression_input)
list_python.append("")
left = list_python[0].count("(")
right = list_python[0].count(")")

print("Valid") if left == right else print("Invalid")
