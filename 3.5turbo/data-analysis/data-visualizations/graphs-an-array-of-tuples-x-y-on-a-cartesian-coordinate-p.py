import matplotlib.pyplot as plt

def plot_coordinates(coordinates):
    # Unpack the coordinates array into separate lists of x and y values
    x_values, y_values = zip(*coordinates)

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot the points on the cartesian coordinate plane
    ax.scatter(x_values, y_values)

    # Add labels and a title to the plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Plotting Coordinates')

    # Adjust the axis limits to fit the data
    ax.autoscale()

    # Display the plot
    plt.show()

# Test the function with sample coordinates
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
plot_coordinates(coordinates)
