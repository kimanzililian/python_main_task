# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK

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
relief=2400
if(taxable_income<=24000):
    payee=(taxable_income*0.1)-relief
elif(taxable_income>24000 and taxable_income<=32333):
    payee=((24000*0.1)+(taxable_income-24000*0.25))-relief
else:
    payee=((24000*0.1)+(8333*0.25)+(taxable_income-32333*0.3))-relief
    print(f"{payee}payee")
