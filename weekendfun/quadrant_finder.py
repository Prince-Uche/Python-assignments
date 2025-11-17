integer_x = int(input("Enter first integer: "))

integer_y = int(input("Enter second integer: "))

if (integer_x > 0 and integer_y > 0):
    print("Q1")

if (integer_x < 0 and integer_y > 0):
    print("Q2")

if (integer_x < 0 and integer_y < 0):
    print("Q3")

if (integer_x > 0 and integer_y < 0):
    print("Q4")

if (integer_x == 0 and integer_y == 0):
    print("Origin")

if (integer_x != 0 and integer_y == 0):
    print("X-axis")

if (integer_x == 0 and integer_y != 0):
    print("Y-axis")






