import random
import heapq

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.g = float('inf')
        self.h = float('inf')
        self.f = float('inf')
        self.parent = None
        self.wall = False

    def __lt__(self, other):
        return self.f < other.f

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        self.start = self.grid[0][0]
        self.end = self.grid[rows-1][cols-1]

    def generate(self):
        for row in self.grid:
            for cell in row:
                if random.random() < 0.3:
                    cell.wall = True

    def heuristic(self, cell):
        return abs(cell.row - self.end.row) + abs(cell.col - self.end.col)

    def get_neighbors(self, cell):
        neighbors = []
        if cell.row > 0:  # up
            neighbors.append(self.grid[cell.row-1][cell.col])
        if cell.row < self.rows - 1:  # down
            neighbors.append(self.grid[cell.row+1][cell.col])
        if cell.col > 0:  # left
            neighbors.append(self.grid[cell.row][cell.col-1])
        if cell.col < self.cols - 1:  # right
            neighbors.append(self.grid[cell.row][cell.col+1])
        return neighbors

    def astar(self):
        open_list = []
        closed_set = set()

        self.start.g = 0
        self.start.h = self.heuristic(self.start)
        self.start.f = self.start.g + self.start.h
        heapq.heappush(open_list, self.start)

        while open_list:
            current = heapq.heappop(open_list)
            if current == self.end:
                path = []
                while current:
                    path.append((current.row, current.col))
                    current = current.parent
                return path[::-1]
            
            closed_set.add(current)
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if neighbor.wall or neighbor in closed_set:
                    continue
                g = current.g + 1
                if g < neighbor.g:
                    neighbor.g = g
                    neighbor.h = self.heuristic(neighbor)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current
                    if neighbor not in open_list:
                        heapq.heappush(open_list, neighbor)

        return None

    def display(self, path):
        for row in self.grid:
            for cell in row:
                if cell == self.start:
                    print("S", end=" ")
                elif cell == self.end:
                    print("E", end=" ")
                elif cell.wall:
                    print("#", end=" ")
                elif (cell.row, cell.col) in path:
                    print(".", end=" ")
                else:
                    print(" ", end=" ")
            print()

if __name__ == "__main__":
    maze = Maze(10, 10)
    maze.generate()
    path = maze.astar()
    if path:
        maze.display(path)
    else:
        print("No path found.")
