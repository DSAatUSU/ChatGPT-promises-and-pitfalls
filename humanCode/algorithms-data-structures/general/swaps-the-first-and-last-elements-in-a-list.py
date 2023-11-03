def swap_first_and_last(test_list):
    test_list[0], test_list[-1] = test_list[-1], test_list[0]
    return test_list


if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    print("The original list is : " + str(test_list))
    print("Modified list: ", swap_first_and_last(test_list))
