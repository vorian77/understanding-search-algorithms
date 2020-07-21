import graph_search
import collections


class SearchAlgo(graph_search.SearchAlgo):
    """Implements Depth First search to provide a path in map from node start to node goal."""
    def __init__(self, map, start, goal):
        super().__init__(map, start, goal)
        self.algorithm_name = "Depth First (First Published: 1800s)"

    def create_scheduled(self):
        """Depth First search implements the scheduler as a stack."""
        return collections.deque()

    def add_to_scheduled(self, node):
        """Adds node to the top of the stack."""
        self.scheduled.append(node)

    def get_next_scheduled(self):
        """Returns the node at the top of the stack."""
        return self.scheduled.pop()

    def get_neighbors(self, node):
        """
        Return the neighbors of node in reverse node_id order so that the
        lower ranked nodes end up closer to the top of the scheduler stack."""
        return sorted(super().get_neighbors(node), reverse=True)

    def process_neighbor(self, current, neighbor):
        """Any visited vertices could be potentially be part of the final search path."""
        self.add_to_path(current, neighbor)

