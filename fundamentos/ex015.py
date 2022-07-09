quilometers = float(input("Quilometers: "))
amount_days = int(input("Days: "))

print(f"\033[38mPay $:\033[34m{(quilometers * 0.15 ) + (amount_days * 60):.2f}")
