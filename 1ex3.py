username=input("Enter username : ")
password=int(input("Enter password : "))

if username=="admin":
    if password==1234:
        print("Access Granted")
else:
    print("Access Denied")

