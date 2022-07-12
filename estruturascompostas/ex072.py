numbers = ("one",  "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty")

while True:
    numberInput = int(input("Write a number between 1 and 20: "))
    if 0 < numberInput <= 20:
        print(numbers[numberInput - 1])
        break
