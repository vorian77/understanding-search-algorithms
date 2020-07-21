from helpers import load_map_10, load_map_40, load_map_simple
import a_star
import uniform_cost
import breath_first
import depth_first


def main():
    """Use this program to compare and contrast four graph searching algorithms."""
    map_40 = load_map_40()
    map_10 = load_map_10()
    map_simple = load_map_simple()

    algorithms = [a_star, uniform_cost, breath_first, depth_first]

    # The loop below will execute the same search using each of the four algorithms.
    # Experiment with different maps and searches to understand the attributes,
    # performance characteristics, and code of each algorithm.
    graph = map_40
    start_node = 5
    goal_node = 34

    print(f"Nodes in Map: {len(graph.intersections)} \n")

    for algo in algorithms:
        method = algo.SearchAlgo(graph, start_node, goal_node)
        method.search()
        print(f"Algorithm: {method.algorithm_name}")
        print(f"Path: {method.path}")
        print(f"Path length: {method.path_length}")
        print(f"Number of nodes visited: {len(method.visited)} ({len(method.visited) / len(method.map.intersections) * 100}%)")
        print(f"Nodes visited:", ', '.join(map(str, method.visited)))
        print("")

if __name__ == "__main__":
    main()
