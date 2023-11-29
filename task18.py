# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF) 
basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))
gross_salary=basic_salary+benefits
print(f"{gross_salary} gross_salary")
if(gross_salary>0 and gross_salary<=18000):
    nssf=gross_salary*0.06
else:
    nssf=18000*0.06
    print(f"{nssf} nssf")
    nhdf=gross_salary*0.015
print(f"{nhdf}nhdf")
taxable_income=gross_salary-(nssf+nhdf)
print(f"{taxable_income}taxable income")