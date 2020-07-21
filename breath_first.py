import graph_search
import collections


class SearchAlgo(graph_search.SearchAlgo):
    """Implements Breath First search to provide a path in map from node start to node goal."""
    def __init__(self, map, start, goal):
        super().__init__(map, start, goal)
        self.algorithm_name = "Breath First (First Published: 1945)"

    def create_scheduled(self):
        """Breath First search implements the scheduler as a queue."""
        return collections.deque()

    def add_to_scheduled(self, node):
        """Adds node to the top of the queue."""
        self.scheduled.appendleft(node)

    def get_next_scheduled(self):
        """Returns the node at the top of the queue."""
        return self.scheduled.pop()

    def get_neighbors(self, node):
        """Returns the neighbors of node in node_id order"""
        return sorted(super().get_neighbors(node))

    def process_neighbor(self, current, neighbor):
        """Any visited vertices could be potentially be part of the final search path."""
        self.add_to_path(current, neighbor)

