import math
D = input("Please input a comma separated sequence of numbers(Ex: 1,2,3,4): ")
D = [int(x) for x in D.split(",")]

C = 50
H = 30

for val in D:
    answer = math.sqrt((2 * C * val)/H)
    print("Q for D(" + str(val) + "): " + str(answer))
