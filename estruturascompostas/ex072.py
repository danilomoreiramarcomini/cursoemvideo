numbers = ("one",  "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty")

while True:
    number_input = int(input("Write a number between 1 and 20: "))
    if 0 < number_input <= 20:
        print(numbers[number_input - 1])
        break
