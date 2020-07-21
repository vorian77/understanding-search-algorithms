import graph_search
import math

class SearchAlgo(graph_search.SearchAlgo):
    """Implements Uniform Cost search which provides shortest possible path in map from the start to the goal node."""
    def __init__(self, map, start, goal):
        super().__init__(map, start, goal)
        self.algorithm_name = "Uniform Cost (First Published: 1959)"

        # Container for storing the priority values for each node in the map,
        # which is the distance from the node back to the start node
        self.g_score = self.create_g_score()

    def create_scheduled(self):
        return set()

    def add_to_scheduled(self, node):
        """Uniform Cost search implements the scheduler as a priority queue.

        This implementation of the priority queue stores scheduled nodes in a set,
        while the retrieval order priority for nodes will be managed through the g_score dictionary
        """
        self.scheduled.add(node)

    def get_next_scheduled(self):
        """Returns the node in the scheduler with the lowest g_score (distance back to the start node)."""
        node = min(self.scheduled, key=self.g_score.get)
        self.scheduled.remove(node)
        return node

    def process_neighbor(self, current, neighbor):
        # Determine if the vertex between current and neighbor should be considered as a
        # component of the solution path. Only include this vertex if paths going though
        # it would be shorter than any paths that go through the neighbor node.
        if self.calculate_gScore(current, neighbor) < self.get_g_score(neighbor):
            self.add_to_path(current, neighbor)

    def add_to_path(self, current, neighbor):
        """Save the vertex between current and neighbor as a search path candidate,
        and calculate and update the g_score (distance between neighbor and the start node)
        for neighbor, so that the algorithm knows the lowest cost possible for any paths that
        traverse through it."""
        super().add_to_path(current, neighbor)
        self.g_score[neighbor] = self.calculate_gScore(current, neighbor)

    # NODE SCORING
    def init_score(self, node_score, start_score):
        """Initializes the dictionary that will be used to store the priority value for each node.
        Sets the start node's value to start_score, and all other values to node_score"""
        score = {key: node_score for key in self.map.intersections}
        score[self.start] = start_score
        return score

    def create_g_score(self):
        """Returns a container initialized to infinity for each node in the map, except the start
        node's value, which is set to 0 (representing no distance between the start node and itself)."""
        return self.init_score(math.inf, 0)

    def get_g_score(self, node):
        """Returns the current g_score of a node (distance back to the start node)"""
        return self.g_score[node]

    def calculate_gScore(self, current, neighbor):
        """Computes and returns the g_score for neighbor, which is the g_score of current (the distance
        between it and the start node) plus the distance between the current and neighbor nodes."""
        return self.g_score[current] + self.distance(current, neighbor)
