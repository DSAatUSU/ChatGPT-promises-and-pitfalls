# Method 1: Using the built-in len() function
def method1(my_list):
    return len(my_list)

# Method 2: Looping through the list and counting the elements
def method2(my_list):
    count = 0
    for _ in my_list:
        count += 1
    return count

# Method 3: Converting the list to a string and counting the characters
def method3(my_list):
    return len(str(my_list))

# Method 4: Using a list comprehension and sum()
def method4(my_list):
    return sum(1 for _ in my_list)

# Method 5: Using the enumerate() function and counting the iterations
def method5(my_list):
    count = 0
    for _, _ in enumerate(my_list):
        count += 1
    return count

# Method 6: Using the range() function and counting the iterations
def method6(my_list):
    count = 0
    for _ in range(len(my_list)):
        count += 1
    return count

# Testing the methods
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(f"Method 1: {method1(my_list)}")
    print(f"Method 2: {method2(my_list)}")
    print(f"Method 3: {method3(my_list)}")
    print(f"Method 4: {method4(my_list)}")
    print(f"Method 5: {method5(my_list)}")
    print(f"Method 6: {method6(my_list)}")
