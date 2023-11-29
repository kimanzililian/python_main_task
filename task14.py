# Write a program that takes input of 2 values and adds them. The program should only accept numbers 
# and floats only or otherwise display an error “invalid character entered” and take the user 
# to re-enter the inputs .

num1=float(input("enter value:"))
num2=float(input("enter value:"))
sum=num1 + num2
if(num1+num2):
    print(f"{sum} sum")
else:
    print("invalid character entered")