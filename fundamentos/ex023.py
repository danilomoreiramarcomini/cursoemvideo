number = int(input("Number: "))

unity = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print(f"• Thousand\033[34m:.....{thousand}\033[38m")
print(f"• Hundred\033[34m:......{hundred}\033[38m")
print(f"• Ten\033[34m:..........{ten}\033[38m")
print(f"• Unity\033[34m:........{unity}\033[38m")
