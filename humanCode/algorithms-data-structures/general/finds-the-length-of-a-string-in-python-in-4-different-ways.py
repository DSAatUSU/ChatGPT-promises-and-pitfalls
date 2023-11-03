# Returns length of string
def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


# Returns length of string
def findLen2(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


# Returns length of string
def findLen3(str):
    if not str:
        return 0
    else:
        some_random_str = "py"
        return ((some_random_str).join(str)).count(some_random_str) + 1

import functools
 
def findLen4(string):
    return functools.reduce(lambda x,y: x+1, string, 0)

if __name__ == "__main__":
    str = "geeks"
    print(findLen(str))
    print(findLen2(str))
    print(findLen3(str))
    print(findLen4(str))
