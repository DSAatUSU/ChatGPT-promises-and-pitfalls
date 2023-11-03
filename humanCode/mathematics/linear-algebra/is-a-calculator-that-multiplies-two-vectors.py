first = input("Input the first vector to multiply, with numbers separated by spaces, (e.g.: 1 2 3 4) ")
second = input("Input the second vector to multiply. Ensure it has the same quantity of numbers as the first one: ")

first = [int(x) for x in first.split()]
second = [int(x) for x in second.split()]

print("Your vector: ")
for i in range(len(first)):
    print(first[i] * second[i])




