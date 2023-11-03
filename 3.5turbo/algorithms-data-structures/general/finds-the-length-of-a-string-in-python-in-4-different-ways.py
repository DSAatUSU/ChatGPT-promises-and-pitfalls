# Method 1:
def get_length_1(string):
    """
    This method uses the built-in len() function to find the length of a string.
    """
    return len(string)


# Method 2:
def get_length_2(string):
    """
    This method uses a loop to count the characters in the string and increment a counter variable.
    """
    count = 0
    for _ in string:
        count += 1
    return count


# Method 3:
def get_length_3(string):
    """
    This method uses recursion to find the length of a string.
    """
    if string == '':
        return 0
    return 1 + get_length_3(string[1:])


# Method 4:
def get_length_4(string):
    """
    This method converts the string to a list and uses the list's built-in length() method to find the length.
    """
    return list(string).__len__()


# Test the methods with an example string
example_string = input("Enter a string: ")

print("Method 1: Length is", get_length_1(example_string))
print("Method 2: Length is", get_length_2(example_string))
print("Method 3: Length is", get_length_3(example_string))
print("Method 4: Length is", get_length_4(example_string))
