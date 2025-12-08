
def menu():
        """         🍕️ WELCOME TO IYA SCAMBIRAH PIZZA JOINT AJEGUNLE 🍕️
 
             Pizza Type:        Slices🍕️:          Price💸️:
             sapa size          4                   #2,000
             small money        6                   #2,400
             big boys           8                   #3,000
             odogwu             12                  #4,200
        """
        return menu.__doc__
print(menu())

get_number = (int(input("How many guests do you have: ")))


get_type = (str(input("What type of pizza do you want: ")).lower())

if get_type == "sapa size":
    slices = 4
elif get_type == "small money":
    slices = 6
elif get_type == "big boys":
    slices = 8
elif get_type == "odogwu":
    slices = 12

if get_type == "sapa size":
    cost = 2000
elif get_type == "small money":
    cost = 2400
elif get_type == "big boys":
    cost = 3000
elif get_type == "odogwu":
    cost = 4200

numbers = get_number // slices
if get_number % slices != 0:
    numbers = get_number // slices
    numbers += 1

leftover_slices = (numbers * slices) - get_number

total_cost = numbers * cost

print(">>> ORDER DETAILS <<<")
print("Pizza Type: ", get_type)
print("Number of guests: ", get_number)
print("Cost per box: ", cost)
print("Number of boxes: ", numbers)
print("Number of left over slices: ", leftover_slices)
print("TOTAL = ", total_cost)




   
