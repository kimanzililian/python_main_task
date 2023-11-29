# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!

num1=input("enter number1:")
num2=input("enter number2:")
num3=input("enter number3:")
if(num1>num2 and num1>num3):
    print(f"{num1} is the largest")
elif(num2>num1 and num2>num3):
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")
