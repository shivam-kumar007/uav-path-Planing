from path_planner import PathPlanner
from environment import Environment
from uav import UAV
import matplotlib.pyplot as plt

def main():
    # Define the environment (grid size, obstacles, etc.)
    grid_size = (10, 10)  # 10x10 grid
    start = (0, 0)  # Start position
    goal = (9, 9)  # Goal position
    obstacles = [(3, 4), (4, 4), (5, 4), (6, 4)]  # Obstacle positions

    # Create environment
    env = Environment(grid_size, obstacles)
    
    # Initialize UAV and Path Planner
    uav = UAV(start)
    planner = PathPlanner(env)

    # Plan the path using Dijkstra's algorithm
    path = planner.plan_path(start, goal)
    
    # Output result
    if path:
        print("Path found:", path)
        plot_path(env, path)
    else:
        print("No path found")

def plot_path(environment, path):
    grid = environment.create_grid()
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color='green', marker='o')
    plt.imshow(grid, cmap='gray_r')
    plt.colorbar()
    plt.title("UAV Path Planning (Dijkstra)")
    plt.show()

if __name__ == "__main__":
    main()
