complete_name = str(input("Complete name: ")). title().strip()
silva = "Silva"
completa_name_list = complete_name.split()

if silva in completa_name_list:
    print("True")
else:
    print("False")
