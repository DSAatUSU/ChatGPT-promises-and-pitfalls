import random
def minimum(a, b):

    if a <= b:
        return a
    else:
        return b

if __name__ == "__main__":
    # Driver code
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print("a = ", a)
    print("b = ", b)
    print("Min: ",minimum(a, b))