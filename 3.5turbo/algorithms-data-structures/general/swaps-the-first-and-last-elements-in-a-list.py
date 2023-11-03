def swap_first_and_last(lst):
    # Check if the list has at least two elements
    if len(lst) >= 2:
        # Swap first and last elements
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Test the function with some sample inputs
my_list = [1, 2, 3, 4, 5]
swapped_list = swap_first_and_last(my_list)
print(swapped_list)
