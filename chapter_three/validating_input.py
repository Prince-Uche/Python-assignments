user_input = int(input("Enter numerical input: "))

passes = 0
failures = 0

while user_input != 1 and user_input != 2:
    print("Invalid number")
    second_input = int(input("Enter a numerical input: "))

if user_input == 1 and user_input == 2:
    print("Congratulations")

if user_input != 1 and user_input == 1:
    passes += 1

if user_input == 1 and user_input != 1:
    passes += 1

else:
    failures += 1

print("Passed:", passes)
print("Failed", failures)
    
# Use one counter to keep track of the number of passes, then calculate the number
#of failures after all the user’s inputs have been received.
