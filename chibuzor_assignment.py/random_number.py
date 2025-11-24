import random

random_number = random.randrange(1, 20)

user_input = int(input("Enter a number: "))

while user_input != random_number:
    if user_input > random_number:
        print("Too high, try again")
    else:
        print("Too low, try again")
    user_input = int(input("Enter a number: "))
    if user_input == random_number:
        print("Correct guess")         
    
