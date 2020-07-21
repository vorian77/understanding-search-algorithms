import math


class SearchAlgo:
    """Template used for implementing graph search algorithms"""

    def __init__(self, map=None, start=None, goal=None):
        """ """
        self.algorithm_name = "base class"

        self.map = map
        self.start = start
        self.goal = goal

        self.scheduled = self.create_scheduled()
        self.add_to_scheduled(self.start)
        self.visited = []  # tracks the nodes that have been visited during search
        self.came_from = {}  # tracks the vertices that have been traversed during search

        self.path = []
        self.path_length = 0.0

    def get_path(self, current):
        """Returns the search plan calculated by the search function.

        Construct the search path (from the start node to the goal node),
        while also calculating the length of the search path.
        """
        total_path = [current]
        while current in self.came_from.keys():
            parent = self.came_from[current]
            total_path.append(parent)
            self.path_length += self.distance(parent, current)
            current = parent
        self.path = [x for x in reversed(total_path)]
        return self.path

    def search(self):
        """Returns a path start node to the goal node, and None if no path exists.

        The search algorithms inherited from this class share the following processing structure:
        1) While there are scheduled nodes to be processed, select one from the list based on
           criteria specific to the algorithm.
           a) Check to see if the selected node is the goal node.
              If it is, exit processing, and build and return the search path.
           b) Otherwise, process the neighbors of the selected node.
              i) Ignore any neighbor that has already been visited.
              ii) If the neighbor has not been scheduled, schedule it based on
                  criteria specific to the algorithm
              iii) Process the neighbor, potentially adding it to the final search path,
                   based on criteria specific to the algorithm.
        """
        while len(self.scheduled) > 0:
            current = self.get_next_scheduled()
            self.visited.append(current)

            if current == self.goal:
                return self.get_path(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.visited:
                    continue

                if neighbor not in self.scheduled:
                    self.add_to_scheduled(neighbor)

                self.process_neighbor(current, neighbor)  # algorithm unique

    # INITIALIZE SCHEDULING CONTAINER
    def create_scheduled(self):
        """Creates and returns a data structure to hold the nodes that have been discovered, but not yet evaluated.

        Also, adds (schedules) the start node, which initiates search traversal of the map.
        """
        pass

    # GENERAL NODE PROCESSING
    def add_to_scheduled(self, node):
        """Adds node to the scheduler (algorithm specific)"""
        pass

    def get_next_scheduled(self):
        """Retrieves, returns, and removes a node from the scheduler (algorithm specific)"""
        pass

    def get_neighbors(self, node):
        """Returns the neighbors of a node (algorithm specific)"""
        return self.map.roads[node]

    def distance(self, node_1, node_2):
        """Returns the Euclidean L2 Distance between node_1 and node_2"""

        # Returns infinity if either node is not in the map
        if node_1 not in self.map.intersections or node_2 not in self.map.intersections:
            return math.inf
        else:
            node_1_pos_x = self.map.intersections[node_1][0]
            node_1_pos_y = self.map.intersections[node_1][1]
            node_2_pos_x = self.map.intersections[node_2][0]
            node_2_pos_y = self.map.intersections[node_2][1]
            return math.sqrt((node_1_pos_x - node_2_pos_x) ** 2 + (node_1_pos_y - node_2_pos_y) ** 2)

    # NEIGHBOR NODE PROCESSING
    def process_neighbor(self, current, neighbor):
        """Determines if a neighbor should be added to the search path (algorithm specific)"""
        pass

    def add_to_path(self, current, neighbor):
        """Saves the vertex between the current and neighbor nodes (algorithm specific).

        The vertex may or may be not be included in the final search path solution.
        """
        self.came_from[neighbor] = current
