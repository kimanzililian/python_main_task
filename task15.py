# Write a program that takes input of someone's basic salary and benefits, adds them 
# to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  

basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))
gross_salary=basic_salary+benefits
print(f"{gross_salary} gross_salary")
nhif=""
# // NHIF calculations
#         let NHIF_calculations;
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