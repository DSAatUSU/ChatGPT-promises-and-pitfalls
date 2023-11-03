def generate_dictionary(n: int) -> dict:
    """
    Generates a dictionary with (i, i x i) pairs for integral numbers between 1 and n.

    Args:
        n (int): The upper limit of the range (inclusive).

    Returns:
        dict: The generated dictionary.
    """
    square_dict = {}

    for i in range(1, n+1):
        square_dict[i] = i * i
    
    return square_dict

if __name__ == "__main__":
    n = int(input("Enter an integral number: "))

    result = generate_dictionary(n)
    print(result)
