import matplotlib.pyplot as plt

def create_discrete_graph():
    # Define x and y values for the graph
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the discrete graph
    ax.plot(x, y, marker='o')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Discrete Graph')

    # Show the graph
    plt.show()

if __name__ == "__main__":
    # Call the function to create and display the graph
    create_discrete_graph()
