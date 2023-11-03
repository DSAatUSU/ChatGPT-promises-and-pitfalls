from operator import length_hint
from collections import Counter
import time


# Define a function to count the number of elements in a list using recursion
def count_elements_recursion(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: add 1 to the count of the remaining elements in the list
    return 1 + count_elements_recursion(lst[1:])


if __name__ == "__main__":
    # Initializing list
    test_list = [1, 4, 5, 7, 8]
    # Printing test_list
    print("The list is : " + str(test_list))

    start_time_naive = time.time()
    counter = 0
    for i in test_list:
        counter = counter + 1
    list_len_naive = counter
    end_time_naive = str(time.time() - start_time_naive)

    start_time_counter = time.time()
    list_len_counter = sum(Counter(test_list).values())
    end_time_counter = str(time.time() - start_time_counter)

    # Finding length of list
    # using len()
    start_time_len = time.time()
    list_len = len(test_list)
    end_time_len = str(time.time() - start_time_len)

    # Finding length of list
    # using length_hint()
    start_time_hint = time.time()
    list_len_hint = length_hint(test_list)
    end_time_hint = str(time.time() - start_time_hint)

    start_time_sum = time.time()
    list_len_sum = sum(1 for i in test_list)
    end_time_sum = str(time.time() - start_time_sum)

    start_time_recursion = time.time()
    list_len_recursion = count_elements_recursion(test_list)
    end_time_recursion = str(time.time() - start_time_recursion)

    start_time_enumerate = time.time()
    list_len_enumerate = 0
    for i, a in enumerate(test_list):
        list_len_enumerate += 1
    end_time_enumerate = str(time.time() - start_time_enumerate)

    # Printing Times of each
    print(
        "Time taken using naive method is : " + end_time_naive,
        " and the length is : " + str(list_len_naive),
    )
    print(
        "Time taken using len() is : " + end_time_len,
        " and the length is : " + str(list_len),
    )
    print(
        "Time taken using length_hint() is : " + end_time_hint,
        " and the length is : " + str(list_len_hint),
    )
    print(
        "Time taken using Counter() is : " + end_time_counter,
        " and the length is : " + str(list_len_counter),
    )
    print(
        "Time taken using sum() is : " + end_time_sum,
        " and the length is : " + str(list_len_sum),
    )
    print(
        "Time taken using recursion is : " + end_time_recursion,
        " and the length is : " + str(list_len_recursion),
    )
    print(
        "Time taken using enumerate is : " + end_time_enumerate,
        " and the length is : " + str(list_len_enumerate),
    )
