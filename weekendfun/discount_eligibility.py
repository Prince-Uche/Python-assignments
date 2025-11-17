total_bill = float(input("What is your total bill: "))

membership = str(input("Are you a member: "))

if (total_bill >= 1000 and membership == "yes"):
    print("You have a discount of 10% off")

if (total_bill >= 1000 and membership == "no"):
    print("You have a discount of 5% off")

else:
    print("you have an AMOUNT OF:", total_bill, "and your MEMBERSHIP IS:", membership, "You are not eligible for a discount")

