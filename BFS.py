import numpy as np

def floodfill(grid, row, column):
    queue = []
    grid[row, column] = 0  # Mark the starting point with distance 0
    queue.append((row, column))  # Add tuple of coordinates to queue
    print(queue)
    
    while queue:
        current_row, current_column = queue[0]  # Get the first element
        del queue[0]  # Remove the first element from the queue using del

        current_distance = grid[current_row, current_column]
        print(current_distance)

        # Neighbors: Up, Down, Left, Right, and Diagonals
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in neighbors:
            new_row, new_column = current_row + dx, current_column + dy
            if 0 <= new_row < grid.shape[0] and 0 <= new_column < grid.shape[1] and grid[new_row, new_column] == -1:
                grid[new_row, new_column] = current_distance + 1
                queue.append((new_row, new_column))

    return grid

# grid = np.full((6,6),-1)
# print(floodfill(grid, 5,5))

def flood_fill_distance(grid, start_row, start_col):
    # Initialize the grid with -1 to indicate unvisited cells
    distance = 0
    grid[start_row, start_col] = distance
    queue = [(start_row, start_col)]
    
    # Define the relative positions of the 4 direct neighbors (up, down, left, right)
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while queue:
        next_queue = []
        for current_row, current_col in queue:
            for dx, dy in neighbors:
                new_row, new_col = current_row + dx, current_col + dy
                # Check if the new cell is within the grid bounds and unvisited
                if 0 <= new_row < grid.shape[0] and 0 <= new_col < grid.shape[1] and grid[new_row, new_col] == -1:
                    grid[new_row, new_col] = distance + 1
                    next_queue.append((new_row, new_col))
        queue = next_queue
        distance += 1
    
    return grid

# Example usage
# rows, cols = 5, 5  # Grid size
# grid = -1 * np.ones((rows, cols), dtype=int)  # Initialize grid with -1

# # Start flood fill from this point
# start_point = (1, 2)  # Arbitrary starting point within the grid
# result_grid = flood_fill_distance(grid, *start_point)

# print(result_grid)
