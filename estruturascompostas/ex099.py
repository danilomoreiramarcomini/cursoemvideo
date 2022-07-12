def bigger(my_list):
    for value in my_list:
        print(f"{value}", end=" ")

    print(f"\nNumber of numbers entered: {len(my_list)} \n"
          f"The bigger value is: {max(my_list)}")


amount_values = int(input("How many numbers do you want to enter: "))

new_list = list()

for number in range(0, amount_values):
    new_list.append(int(input("Number: ")))

bigger(new_list)
