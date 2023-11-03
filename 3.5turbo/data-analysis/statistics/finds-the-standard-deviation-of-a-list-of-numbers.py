import statistics

def calculate_std_deviation(numbers):
    return statistics.stdev(numbers)

if __name__ == '__main__':
    # Get input from the user
    num_list = input("Enter a list of numbers (separated by space): ").split()

    # Convert input to list of floats
    try:
        num_list = list(map(float, num_list))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        exit()

    # Calculate standard deviation
    std_deviation = calculate_std_deviation(num_list)
    print(f"The standard deviation of the given numbers is: {std_deviation}")
