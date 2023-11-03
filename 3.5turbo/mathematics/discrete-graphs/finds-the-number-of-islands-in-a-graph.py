def get_neighbors(matrix, rows, cols, i, j):
    # Define the possible directions to explore in the matrix
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    
    for direction in directions:
        x, y = i + direction[0], j + direction[1]
        
        # Check if the neighbor is within the matrix boundaries
        if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1:
            neighbors.append((x, y))
    
    return neighbors

def dfs(matrix, rows, cols, i, j, visited):
    # Mark the current cell as visited
    visited[i][j] = True
    
    # Get the neighbors of the current cell
    neighbors = get_neighbors(matrix, rows, cols, i, j)
    
    # Explore each neighbor recursively
    for neighbor in neighbors:
        x, y = neighbor
        
        # Continue DFS exploration if the neighbor is not visited
        if not visited[x][y]:
            dfs(matrix, rows, cols, x, y, visited)

def count_islands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a matrix to keep track of visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    island_count = 0
    
    # Iterate over each cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # If the cell is land and not visited, increase island count and perform DFS
            if matrix[i][j] == 1 and not visited[i][j]:
                island_count += 1
                dfs(matrix, rows, cols, i, j, visited)
    
    return island_count

# Test the code
# Example matrix: [[1, 1, 0, 0, 0],
#                  [0, 1, 0, 0, 1],
#                  [1, 0, 0, 1, 1],
#                  [0, 0, 0, 0, 0],
#                  [1, 0, 1, 0, 1]]
matrix = [
    [1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 1], 
    [1, 0, 0, 1, 1], 
    [0, 0, 0, 0, 0], 
    [1, 0, 1, 0, 1]
]
island_count = count_islands(matrix)
print("Number of islands:", island_count)
