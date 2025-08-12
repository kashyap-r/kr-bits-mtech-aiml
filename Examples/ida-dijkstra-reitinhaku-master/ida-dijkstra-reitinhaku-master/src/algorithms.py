from queue import PriorityQueue
import math


def dijkstra(graph, start, goal):
    """A function for finding the shortest path to the end vertix from the starting vertices
    using Dijkstra's algorithm.

    Args:
        graph: The graph you want to find the shortest paths in.
        start: The starting vertix for the algorithm.
        goal: End vertix.

    Returns:
        A list of the shortest path to all of the nodes in the graph.
    """

    distances = {v: float("inf") for v in range(graph.node_amount)}
    distances[start] = 0
    previous = [[] for _ in range(graph.node_amount)]

    path = []

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():

        (val, current) = pq.get()

        graph.seen.append(current)

        for neighbor in range(graph.node_amount):
            if graph.edge[current][neighbor] != -1:
                distance = graph.edge[current][neighbor]
                if neighbor not in graph.seen:
                    old_cost = distances[neighbor]
                    new_cost = distances[current] + distance

                    if new_cost < old_cost:
                        previous[neighbor] = current

                        pq.put((new_cost, neighbor))
                        distances[neighbor] = new_cost

    p = goal
    path.append(p)

    while True:
        if previous[p] == start:
            break

        path.append(previous[p])
        p = previous[p]
    path.append(start)
    path.reverse()

    return distances, path


def heuristic_value(x1, y1, x2, y2):
    """Returns the euclidean distance for IDA* to use as a heuristic value

    Args:
        x: current 
        y: goal

    Returns:
        Euclidean distance
    """

    weight = math.sqrt(((x2-x1)
                        ** 2 + (y2 - y1)**2))
    return weight


def ida_star(graph, start, goal):
    """IDA*- pathfinding algorithm.

    Args:
        graph: Graph-class object, which represents a graph.
        start: The starting node for the algorithm.
        goal: The goal node for the algorithm.

    Returns:
        integer: Returns the distance from starting node to the goal node.
    """
    max = heuristic_value(
        graph.nodes[start][0], graph.nodes[start][1], graph.nodes[goal][0], graph.nodes[goal][1])

    print ('Kashyap heuristic params')
    print (f"{graph.nodes[start][0]}, {graph.nodes[start][1]}, {graph.nodes[goal][0]}, {graph.nodes[goal][1]}")
    print (f"Heuristic Value={max}")


    while True:
        distance = ida_search(graph, start, goal, 0, max)
        if distance == float("inf"):
            return -1
        elif distance < 0:
            print("Found!")
            return -distance
        else:
            max = distance


def ida_search(graph, vertix, goal, distance, max):
    """The actual searching method, depth-first search with heuristic values
    to choose optimal paths.
    """
    print("Visiting vertix " + str(vertix))

    if vertix == goal:
        return -distance
    visited_nodes = []

    estimate = distance + \
        heuristic_value(graph.nodes[vertix][0], graph.nodes[vertix]
                        [1], graph.nodes[goal][0], graph.nodes[goal][1])
    # print(estimate)
    if estimate > max:
        # print("Max cost reached:" + str(estimate))
        return estimate

    min = float("inf")

    for i in range(graph.node_amount):
        print 
        if graph.edge[vertix][i] != -1:
            if i not in visited_nodes:
                visited_nodes.append(i)
                val = ida_search(graph, i, goal,
                                 distance + graph.edge[vertix][i], max)
                if val < 0:
                    return val
                elif val < min:
                    min = val

    return min
