# This program generates a user-defined number of random numbers, between 0 and a user defined max.

import random

selected_range = int(input("Select the upper limit of the range:\n"))
selected_number = int(input("How many numbers would you like to generate?\n"))

number_list = []

for i in range(selected_number):
    number_list.append(random.randint(0, selected_range))
print(number_list)

with open('random.numbers.txt', 'w') as f:
    f.write(str(number_list))
    f.close()
