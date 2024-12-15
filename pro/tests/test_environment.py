import unittest
from environment import Environment

class TestEnvironment(unittest.TestCase):
    
    def setUp(self):
        """Set up the environment for testing."""
        grid_size = (5, 5)
        obstacles = [(2, 2), (2, 3), (3, 2)]
        self.env = Environment(grid_size, obstacles)
        
    def test_is_free(self):
        """Test if the environment correctly identifies free and occupied spaces."""
        # Test free position
        self.assertTrue(self.env.is_free((0, 0)), "Position (0, 0) should be free.")
        
        # Test obstacle position
        self.assertFalse(self.env.is_free((2, 2)), "Position (2, 2) should be blocked.")
        
        # Test boundary position
        self.assertFalse(self.env.is_free((5, 5)), "Position (5, 5) should be out of bounds.")
        
    def test_create_grid(self):
        """Test if the grid is created correctly with obstacles."""
        grid = self.env.create_grid()
        
        # Check grid size
        self.assertEqual(len(grid), 5, "Grid should have 5 rows.")
        self.assertEqual(len(grid[0]), 5, "Grid should have 5 columns.")
        
        # Check obstacle positions
        self.assertEqual(grid[2][2], -1, "Obstacle should be at position (2, 2).")
        self.assertEqual(grid[2][3], -1, "Obstacle should be at position (2, 3).")
        self.assertEqual(grid[3][2], -1, "Obstacle should be at position (3, 2).")
        
if __name__ == "__main__":
    unittest.main()
