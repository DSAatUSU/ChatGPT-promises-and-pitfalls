import statistics

# Get user input for list of numbers
numbers = input("Enter numbers separated by a space: ").split()
numbers = [int(num) for num in numbers]

# Calculate the average of the numbers
average = statistics.mean(numbers)

# Calculate the distance of each number from the average
distances = [abs(num - average) for num in numbers]

# Display the distances
for i, num in enumerate(numbers):
    distance = distances[i]
    print(f"The distance of {num} from the average is {distance}")
