if __name__ == "__main__":

    # initializing string
    test_str = str(input("Enter a string: "))
    letter = str(input("Enter a letter: "))

    # using lambda + sum() + map() to get count
    # counting e
    count = sum(map(lambda x: 1 if letter in x else 0, test_str))

    # printing result
    print(f"Count of {letter} in '{test_str}' is : " + str(count))
