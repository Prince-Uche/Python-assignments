age = int(input("Enter age: "))

if (age < 5):
    print("Ticket price is free")

elif (age > 4 and age < 13):
    print("Tiecket price is $5")

elif (age > 12 and age < 65):
    print("Ticket price is $12")

elif (age > 64):
    print("Ticket price is $8")

else:
    print("Invalid option")
