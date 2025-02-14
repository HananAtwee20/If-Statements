age=int(input("Enter your age : "))

if age>=25:
   print("Ticket price is 20$")
elif age>=20:
    print("Ticket price is 15$")
elif age>=15:
    print("Ticket price is 10$")
elif age>=10:
    print("Ticket price is 5$")
else:
    print("No ticket needed")