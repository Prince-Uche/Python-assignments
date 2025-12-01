def multiplication(first_input, second_input):
    product = 0
    for number in range(1, second_input + 1, 1):
        product += first_input        
    return product
first_input = int(input("Enter first number: "))
second_input = int(input("Enter second number: "))
print(multiplication(first_input, second_input))
