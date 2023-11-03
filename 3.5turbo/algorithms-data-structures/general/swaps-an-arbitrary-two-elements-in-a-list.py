def swap_elements(lst, index1, index2):
    """
    Swaps the elements at index1 and index2 in the given list.
    
    Args:
        lst (list): The list in which the elements should be swapped.
        index1 (int): The index of the first element to swap.
        index2 (int): The index of the second element to swap.
        
    Returns:
        The modified list with swapped elements.
    """
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst


if __name__ == "__main__":
    # Test the function
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    
    index_1 = int(input("Enter the index of the first element to swap: "))
    index_2 = int(input("Enter the index of the second element to swap: "))
    
    if index_1 < 0 or index_1 >= len(my_list) or index_2 < 0 or index_2 >= len(my_list):
        print("Invalid index! Please enter valid indices within the range of the list.")
    else:
        swapped_list = swap_elements(my_list, index_1, index_2)
        print("List after swapping elements:", swapped_list)
