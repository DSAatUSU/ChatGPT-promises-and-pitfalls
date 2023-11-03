def print_half_diamond(N):
    # Print the upper half diamond
    for i in range(1, N+1):
        print('*' * i)

    # Print the lower half diamond
    for i in range(N-1, 0, -1):
        print('*' * i)

# Get user input for the maximum number of stars at the peak
N = int(input('Enter the maximum number of stars at the peak: '))

# Validate the input
if N < 1:
    print('Invalid input! Please enter a positive integer.')
else:
    # Print the half diamond star pattern
    print_half_diamond(N)
