import numpy as np

def calculate_distances(numbers):
    # calculate the standard deviation
    std_dev = np.std(numbers)

    # calculate the distances from the standard deviation for each number
    distances = [abs(num - std_dev) for num in numbers]

    return distances

# sample list of numbers
numbers = [1, 2, 3, 4, 5]

# calculate and print the distances
distances = calculate_distances(numbers)
print(distances)
