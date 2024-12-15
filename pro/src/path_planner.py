import heapq
from typing import List, Tuple

class PathPlanner:
    def __init__(self, environment):
        self.env = environment

    def plan_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        # Dijkstra's algorithm implementation
        open_list = []
        closed_list = set()
        came_from = {}
        g_score = {start: 0}

        heapq.heappush(open_list, (g_score[start], start))

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            closed_list.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in closed_list or not self.env.is_free(neighbor):
                    continue

                tentative_g_score = g_score[current] + 1  # Uniform cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_list, (g_score[neighbor], neighbor))

        return []  # No path found

    def get_neighbors(self, node: Tuple[int, int]) -> List[Tuple[int, int]]:
        # Possible movement directions (up, down, left, right)
        x, y = node
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        return neighbors

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
