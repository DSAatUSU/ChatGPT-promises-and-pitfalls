def invert_rgb(rgb):
    """
    Function to invert an RGB value represented by a tuple.

    Arguments:
    rgb -- Tuple representing an RGB value

    Returns:
    Tuple representing the inverted RGB value
    """
    inverted_rgb = tuple(255 - value for value in rgb)
    return inverted_rgb


# Test case
rgb_value = (164, 194, 244)
inverted_rgb_value = invert_rgb(rgb_value)
print(f"Inverted RGB value: {inverted_rgb_value}")
