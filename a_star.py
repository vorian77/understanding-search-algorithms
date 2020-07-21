import uniform_cost
import math


class SearchAlgo(uniform_cost.SearchAlgo):
    def __init__(self, map, start, goal):
        """Implements A-Star search, an refinement to Uniform Cost search, which provides the shortest possible
        path in map from the start to the goal node with the fewest possible visited nodes ."""
        super().__init__(map, start, goal)
        self.algorithm_name = "A-Star (First Published: 1968)"

        # Container for storing the priority values for each node in the map,
        # which is the distance from the node back to the start node,
        # plus the Euclidean distance from the node to the goal node
        self.f_score = self.create_f_score()

    def get_next_scheduled(self):
        """Returns the node in the scheduler with the lowest f_score
        (distance back to the start node + Euclidean distance to the goal node)."""
        node = min(self.scheduled, key=self.f_score.get)
        self.scheduled.remove(node)
        return node

    def add_to_path(self, current, neighbor):
        """Save the vertex between current and neighbor as a search path candidate,
        and calculate and update it's f_score (distance back to the start node +
        Euclidean distance to the goal node), so that the algorithm knows the lowest
        cost possible for any paths that traverse through it."""
        super().add_to_path(current, neighbor)
        self.f_score[neighbor] = self.calculate_fscore(neighbor)

    # NODE SCORING
    def create_f_score(self):
        """Returns a container initialized to infinity for each node in the map, except the start
        node's value, which is set it's f_score (distance between it and the goal node)."""
        return self.init_score(math.inf, self.heuristic_cost_estimate(self.start))

    def heuristic_cost_estimate(self, node):
        """Returns H(node), the distance between node and the goal node"""
        return self.distance(node, self.goal)

    def calculate_fscore(self, node):
        """Computes and returns the distance of going through the current node to the neighbor node plus
        the Eucldean distance to the goal node, so that the algorithm can select the shorter path between
        it and the existing shortest paths from the start node to the neighbor node.
        The f_score can be expressed as F = G + H"""
        return self.g_score[node] + self.heuristic_cost_estimate(node)
