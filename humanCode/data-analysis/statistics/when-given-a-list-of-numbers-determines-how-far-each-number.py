if __name__ == '__main__':

    list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    mean_of_nums = sum(list_of_nums) / len(list_of_nums)
    print(f"The following list of numbers {list_of_nums} has a mean of {mean_of_nums}")
    print("Each number in the list is the following distance from the mean:")
    print([abs(mean_of_nums - num) for num in list_of_nums])