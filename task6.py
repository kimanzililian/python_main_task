# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.

password=input("enter password")
correct_password="admin@123"
attempts=3

for i in range(attempts):
    password=in