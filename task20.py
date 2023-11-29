# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))
gross_salary=basic_salary+benefits
print(f"{gross_salary} gross_salary")
if(gross_salary<=5999):
           nhif=150
        
elif(gross_salary<=7999 and gross_salary>5999):
            nhif=300
        
elif(gross_salary<=11999 and gross_salary>7999):
             nhif=400
elif(gross_salary<=14999 and gross_salary>11999):
            nhif=500
        
elif(gross_salary<=19999 and gross_salary>14999):
            nhif=600
        
elif(gross_salary<=24999 and gross_salary>19999):
            nhif=750
        
elif(gross_salary<=29999 and gross_salary>24999):
            nhif=850
        
elif(gross_salary<=34999 and gross_salary>29999):
            nhif=900
        
elif(gross_salary<=39999 and gross_salary>34999):
            nhif=950
        
elif(gross_salary<=44999 and gross_salary>39999):
            nhif=1000
        
elif(gross_salary<=49999 and gross_salary>44999):
            nhif=1100
        
elif(gross_salary<=59999 and gross_salary>49999):
            nhif=1200
        
elif(gross_salary<=69999 and gross_salary>59999):
            nhif=1300
        
elif(gross_salary<=79999 and gross_salary>69999):
            nhif=1400
        
elif(gross_salary<89999 and gross_salary>79999):
            nhif=1500
        
elif(gross_salary<99999 and gross_salary>89999):
            nhif=1600
        
else :
            nhif=1700
        
print(f"{nhif} nhif")
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
net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
print(f"{net_salary}net_salary")