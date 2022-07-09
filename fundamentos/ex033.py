first_number = int(input("First number: "))
second_number = int(input("Second number: "))
third_number = int(input("Third number: "))

if first_number > second_number and first_number > third_number:
    if second_number > third_number:
        biggest_number = first_number
        smallest_number = third_number
        print(f"Biggest number: {biggest_number}")
        print(f"Smallest number: {smallest_number}")
    else:
        biggest_number = first_number
        smallest_number = second_number
        print(f"Biggest number: {biggest_number}")
        print(f"Smallest number: {smallest_number}")

if second_number > first_number and second_number > third_number:
    if first_number > third_number:
        biggest_number = second_number
        smallest_number = third_number
        print(f"Biggest number: {biggest_number}")
        print(f"Smallest number: {smallest_number}")
    else:
        biggest_number = second_number
        smallest_number = first_number
        print(f"Biggest number: {biggest_number}")
        print(f"Smallest number: {smallest_number}")

if third_number > first_number and third_number > second_number:
    if second_number > first_number:
        biggest_number = third_number
        smallest_number = first_number
        print(f"Biggest number: {biggest_number}")
        print(f"Smallest number: {smallest_number}")
    else:
        biggest_number = third_number
        smallest_number = second_number
        print(f"Biggest number: {biggest_number}")
        print(f"Smallest number: {smallest_number}")
