def compute_mean(list_nums):
    """Computes the mean of a list of numbers.

    Args:
        list_nums: A list of numbers.

    Returns:
        The mean of the list of numbers.
    """
    return sum(list_nums) / len(list_nums)


def compute_median(list_nums):
    """Computes the median of a list of numbers.

    Args:
        list_nums: A list of numbers.

    Returns:
        The median of the list of numbers.
    """
    sorted_list = sorted(list_nums)
    if len(sorted_list) % 2 == 0:
        return (
            sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]
        ) / 2
    else:
        return sorted_list[len(sorted_list) // 2]


def compute_mode(list_nums):
    """Computes the mode of a list of numbers.

    Args:
        list_nums: A list of numbers.

    Returns:
        The mode of the list of numbers.
    """
    num_counts = {}
    for num in list_nums:
        if num not in num_counts:
            num_counts[num] = 0
        num_counts[num] += 1
    max_count = 0
    mode = None
    for num in num_counts:
        if num_counts[num] > max_count:
            max_count = num_counts[num]
            mode = num
    return mode


def compute_range(list_nums):
    """Computes the range of a list of numbers.

    Args:
        list_nums: A list of numbers.

    Returns:
        The range of the list of numbers.
    """
    return max(list_nums) - min(list_nums)


if __name__ == "__main__":
    temp_list = [1, 2, 3, 4, 5]

    print("Mean of the list of numbers:", temp_list, "is", compute_mean(temp_list))
    print("Median of the list of numbers:", temp_list, "is", compute_median(temp_list))
    print("Mode of the list of numbers:", temp_list, "is", compute_mode(temp_list))
    print("Range of the list of numbers:", temp_list, "is", compute_range(temp_list))
