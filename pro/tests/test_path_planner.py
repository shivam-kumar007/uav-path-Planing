import unittest
from path_planner import PathPlanner
from environment import Environment

class TestPathPlanner(unittest.TestCase):
    
    def setUp(self):
        """Set up environment and PathPlanner for testing."""
        grid_size = (5, 5)
        obstacles = [(2, 2), (2, 3), (3, 2)]
        self.env = Environment(grid_size, obstacles)
        self.planner = PathPlanner(self.env)
        
    def test_plan_path_success(self):
        """Test if the planner finds a path from start to goal."""
        start = (0, 0)
        goal = (4, 4)
        path = self.planner.plan_path(start, goal)
        self.assertGreater(len(path), 0, "Path should be found.")
        
    def test_plan_path_failure(self):
        """Test if the planner returns no path when there's no valid path."""
        start = (0, 0)
        goal = (2, 3)  # The obstacle is in the way
        path = self.planner.plan_path(start, goal)
        self.assertEqual(path, [], "No path should be found due to obstacles.")
        
    def test_plan_path_multiple_obstacles(self):
        """Test path planning with multiple obstacles."""
        start = (0, 0)
        goal = (4, 4)
        path = self.planner.plan_path(start, goal)
        self.assertGreater(len(path), 0, "Path should be found even with multiple obstacles.")

if __name__ == "__main__":
    unittest.main()
