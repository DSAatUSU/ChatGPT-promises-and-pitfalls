import random


def swap_arbitrary_elements(list_to_swap):
    index1 = random.randint(0, len(list_to_swap) - 1)
    index2 = random.randint(0, len(list_to_swap) - 1)
    while index1 == index2:
        index2 = random.randint(0, len(list_to_swap) - 1)
    list_to_swap[index1], list_to_swap[index2] = (
        list_to_swap[index2],
        list_to_swap[index1],
    )
    return list_to_swap


if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Original list:", test_list)
    swapped_list = swap_arbitrary_elements(test_list)
    print("List after swapping elements:", swapped_list)
