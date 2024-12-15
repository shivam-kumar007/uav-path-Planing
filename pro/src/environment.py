from typing import List, Tuple

class Environment:
    def __init__(self, grid_size: Tuple[int, int], obstacles: List[Tuple[int, int]]):
        self.grid_size = grid_size
        self.obstacles = obstacles

    def is_free(self, position: Tuple[int, int]) -> bool:
        """Check if the position is free (not an obstacle)."""
        if 0 <= position[0] < self.grid_size[0] and 0 <= position[1] < self.grid_size[1]:
            return position not in self.obstacles
        return False

    def create_grid(self):
        """Create a grid with obstacles marked."""
        grid = [[0 for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]
        for (x, y) in self.obstacles:
            grid[x][y] = -1  # Mark obstacles
        return grid
