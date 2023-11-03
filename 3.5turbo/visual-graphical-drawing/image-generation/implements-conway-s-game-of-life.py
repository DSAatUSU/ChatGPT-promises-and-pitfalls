import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the grid
N = 100
# Define the number of generations to simulate
generations = 100

# Create a random initial grid
grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)

# Function to update the grid for each generation
def update_grid(frame_number, grid, N):
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Count the number of live neighbors for each cell
            neighbors = (
                grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]
            )
            # Apply the 3 rules of Conway's Game of Life
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    # Update the grid
    mat.set_data(new_grid)
    grid[:] = new_grid[:]
    return mat

# Create a figure and axis
fig, ax = plt.subplots()
# Create a colormap
cmap = plt.cm.binary
# Create a matrix plot
mat = ax.matshow(grid, cmap=cmap)
# Set the axis labels
ax.set_xticks([])
ax.set_yticks([])

# Create the animation
ani = animation.FuncAnimation(fig, update_grid, fargs=(grid, N, ),
                              frames=generations, interval=100, save_count=50)

# Show the animation
plt.show()
