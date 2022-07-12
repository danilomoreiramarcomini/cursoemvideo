import statistics

name = []
year = []
gender = []
for i in range(1, 5):
    print(f"============ People {i} ============")
    name_input = input(f"Name: ")
    year_input = int(input(f"Age: "))
    gender_input = input(f"Gender: ").upper()
    name.append(name_input)
    year.append(year_input)
    gender.append(gender_input)

print(f"\nThe average age is \033[34m{statistics.median(year)}")

if gender[0] == "M" or gender[1] == "M" or gender[2] == "M" or gender[3] == "M" and year[0] > year[1] and\
        year[0] > year[2] and year[0] > year[3]:
    print(f"{name[0]}\033[38m is the old man")
elif gender[0] == "M" or gender[1] == 'M' or gender[2] == "M" or gender[3] == "M" and year[1] > year[0] and\
        year[1] > year[2] and year[1] > year[3]:
    print(f"{name[1]}\033[38m is the old man")
elif gender[0] == "M" or gender[1] == 'M' or gender[2] == "M" or gender[3] == "M" and year[2] > year[0] and\
        year[2] > year[1] and year[2] > year[3]:
    print(f"{name[2]}\033[38m is the old man")
elif gender[0] == "M" or gender[1] == "M" or gender[2] == "M" or gender[3] == "M" and year[3] > year[0] and\
        year[3] > year[1] and year[3] > year[2]:
    print(f"{name[3]}\033[38m is the old man")
