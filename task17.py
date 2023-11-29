# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))
gross_salary=basic_salary+benefits
print(f"{gross_salary} gross_salary")
nhdf=gross_salary*0.015
print(f"{nhdf}nhdf")
