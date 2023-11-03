# Function to print next generation
def nextGeneration(grid, M, N):
    future = [[0 for i in range(N)] for j in range(M)]

    # Loop through every cell
    for l in range(M):
        for m in range(N):

            # finding no Of Neighbours that are alive
            aliveNeighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (l + i >= 0 and l + i < M) and (m + j >= 0 and m + j < N):
                        aliveNeighbours += grid[l + i][m + j]

            # The cell needs to be subtracted from
            # its neighbours as it was counted before
            aliveNeighbours -= grid[l][m]

            # Implementing the Rules of Life

            # Cell is lonely and dies
            if (grid[l][m] == 1) and (aliveNeighbours < 2):
                future[l][m] = 0

            # Cell dies due to over population
            elif (grid[l][m] == 1) and (aliveNeighbours > 3):
                future[l][m] = 0

            # A new cell is born
            elif (grid[l][m] == 0) and (aliveNeighbours == 3):
                future[l][m] = 1

            # Remains the same
            else:
                future[l][m] = grid[l][m]

    print("Next Generation")
    for i in range(M):
        for j in range(N):
            if future[i][j] == 0:
                print(".", end="")
            else:
                print("*", end="")
        print()


M, N = 10, 10

# Initializing the grid.
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Displaying the grid
print("Original Generation")
for i in range(M):
    for j in range(N):

        if grid[i][j] == 0:
            print(".", end="")
        else:
            print("*", end="")
    print()
print()
nextGeneration(grid, M, N)

# This code is contributed by shinjanpatra
