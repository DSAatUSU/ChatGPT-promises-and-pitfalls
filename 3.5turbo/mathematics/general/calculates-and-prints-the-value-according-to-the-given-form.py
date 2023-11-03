import math

def calculate_Q(D):
    C = 50
    H = 30
    Q = math.sqrt((2 * C * D) / H)
    return Q

def main():
    # Ask the user for input
    values = input("Enter the values of D (comma-separated): ").split(",")
    
    results = []
    for value in values:
        try:
            # Convert the input value to float
            D = float(value)
            Q = calculate_Q(D)
            results.append(Q)
        except ValueError:
            print(f"Invalid input: {value}")
    
    # Print the results
    for i, value in enumerate(results):
        print(f"Q{i+1} = {value:.2f}")

if __name__ == "__main__":
    main()
