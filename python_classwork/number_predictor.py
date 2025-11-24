user_input = int(input("Enter a value: "))

fixed_value = 50

while user_input != fixed_value:
    if user_input > fixed_value:
        print("Too high")
    else:
        print("Too low")
    user_input = int(input("Enter a value: "))

if user_input == fixed_value:
        print(user_input, "is the correct value")
