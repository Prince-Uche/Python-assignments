user_input = input("Enter numbers: ")

for digit in user_input:
    print(digit.count(digit) > 0)
