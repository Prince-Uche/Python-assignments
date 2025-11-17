first_integer = int(input("Enter first integer: "))

second_integer = int(input("Enter second integer: "))

third_integer = int(input("Enter third integer: "))

print('Sum =', first_integer + second_integer + third_integer)

print('Average =', (first_integer + second_integer + third_integer) / 3)

print('Product =', first_integer * second_integer * third_integer)

if first_integer > second_integer and first_integer > third_integer:
    print(first_integer, 'is the largest')

if second_integer > third_integer and second_integer > first_integer:
    print(second_integer, 'is the largest')

if third_integer > first_integer and third_integer > second_integer:
    print(third_integer, 'is the largest')

if first_integer < second_integer and first_integer < third_integer:
    print(first_integer, 'is the smallest')

if second_integer < third_integer and second_integer < first_integer:
    print(second_integer, 'is the smallest')

else: print(third_integer, 'is the smallest')
