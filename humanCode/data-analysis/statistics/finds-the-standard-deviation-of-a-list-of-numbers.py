def standard_deviation(list_of_nums):
    """Computes the standard deviation of a list of numbers.

    Args:
        list_of_nums: A list of numbers.

    Returns:
        The standard deviation of the list of numbers.
    """
    mean_of_nums = sum(list_of_nums) / len(list_of_nums)
    return (
        sum([(num - mean_of_nums) ** 2 for num in list_of_nums]) / len(list_of_nums)
    ) ** 0.5


if __name__ == "__main__":
    list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(
        f"Standard deviation of the list of numbers {list_of_nums} is:",
        standard_deviation(list_of_nums),
    )
