
def calc_gross(benefits,basic_salary):
    gross_salary=basic_salary+benefits
    return gross_salary

print(calc_gross(10000,1000))

# 
basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))
gross_salary=calc_gross(basic_salary,benefits)
print(gross_salary)