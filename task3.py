phone_number=input("enter phone number:")
# 254
if(phone_number[0:4]=="254" and len(phone_number)==13):
    valid=(f"valid phone number{phone_number}")
    print(valid)
    # 07 and 01
elif((phone_number[0:2]=="07" and len(phone_number)==10)or
     (phone_number[0:2]=="0.1" and len(phone_number)==10)
     ):
    new_p= ("+254" + phone_number[1:])
    valid=f"{new_p} is valid"
    print(valid)
elif((phone_number[0:1]=="7") and len((phone_number)==9)or
     (phone_number[0:1]=="1" and len(phone_number)==9)
     ):
    new_p="+254" + phone_number
    valid=f"{new_p} is valid"
    print(valid)
elif(phone_number[0:3]=="254" and len(phone_number)==12):
    new_p="+" + phone_number
    valid=f"{new_p} is valid"
    print(valid)
else:
    print("invalid number")
      