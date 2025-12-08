#sapa_size = [4, 2000]
#small_money = [6, 2400]
#big_boys = [8, 3000]
#ododgwu = [12, 4200]
#
mainmenu = menu()
print(mainmenu)
guests = get_number()
print(guests)
pizzas = get_type()
print(pizzas)
slices = get_slices()
print(slices)




def menu():
        """         🍕️ WELCOME TO IYA SCAMBIRAH PIZZA JOINT AJEGUNLE 🍕️
 
             Pizza Type:        Slices🍕️:          Price💸️:
             sapa size          4                   #2,000
             small money        6                   #2,400
             big boys           8                   #3,000
             odogwu             12                  #4,200
        """
        return menu.__doc__


def get_number(pizza):
    guest_number = int(input("How many guests do you have: "))
    return guest_number

def get_type():
    pizza_type = str(input("What type of pizza do you want: ")).lower()
    return pizza_type

def get_slices(slices):
    if get_type(pizza) == "sapa size":
        slices = 4
    elif get_type(pizza) == "small money":
        slices = 6
    elif get_type(pizza) == "big boys":
        slices = 8
    elif get_type(pizza) == "odogwu":
        slices = 12
    return slices

def get_cost(cost):
    if get_type(pizza) == "sapa size":
        cost = 2000
    elif get_type(pizza) == "small money":
        slices = 2400
    elif get_type(pizza) == "big boys":
        slices = 3000
    elif get_type(pizza) == "odogwu":
        slices = 4200
    return slices

def get_boxes_number(number):
    numbers = get_number(number) //  get_slices(slices)
    if get_number(number) % get_slices(slices) != 0:
        numbers += 1
    return numbers

def get_leftover(leftover):
    leftover_slices = (get_boxes_number(number) * get_slices(slices)) - get_number(number)
    return leftover_slices

def get_total(total):
    total_cost = get_boxes_number(number) * get_cost(cost)
    return total_cost

def reciept(details):
    print("Pizza Type: ", get_type(pizza))
    print("Number of guests: ", get_number(number))
    print("Cost per box: ", get_cost(cost))
    print("Number of boxes: ", get_boxes_number(number))
    print("TOTAL = ", get_total(total))
    return reciept

mainmenu = menu()
print(mainmenu)
guests = get_number()
print(guests)
pizzas = get_type()
print(pizzas)
slices = get_slices()
print(slices)




  
