from numpy import std

myList = range(15)
stdList = []

std = std(myList)

for i in range(len(myList)):
    stdList.append(abs(std - i))

print(stdList)
