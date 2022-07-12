student = dict()

student["name"] = str(input("Name: ").title())
student["average"] = float(input("Averege: "))


if student["average"] >= 7:
    student["status"] = str("\033[34mApproved")
else:
    student["status"] = str("\033[31mDisapproved")

print(f"Student:{student['name']}\n"
      f"Averege:{student['average']}\n"
      f"Stauts:{student['status']}")
