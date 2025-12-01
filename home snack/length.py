import random
new_list = 10

random_number = random.sample(range(1, 50), new_list)

length = 0
for count in random_number:
    length +=1
    print(length)


