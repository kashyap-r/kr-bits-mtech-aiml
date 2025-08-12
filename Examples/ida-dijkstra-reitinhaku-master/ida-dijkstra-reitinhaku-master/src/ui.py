from graph import Graph
import algorithms
import networkx as nx
import netxfuncs as nxf


def start():
    while True:

        # Choose graph node amount, 5-10 for easily readable graphs, more for better testing of algorithms
        print("Choose graph size (Node amount):")

        node_amount = int(input())

        testGraph = Graph(node_amount)

        testGraph.generate_nodes(node_amount)
        testGraph.generate_edges(node_amount)

        print("Choose the indexes of start and end nodes:")
        print("Start node: ")
        start_node = int(input())
        print("End node: ")
        end_node = int(input())

        print ('Kashyap Edges')
        print (testGraph.edge)
        print (f"kashyap nodes")
        print (testGraph.nodes)

        while True:
            print(
                "Choose which algorithm to use, Dijkstra = 1 or IDA* = 2, change start/end nodes = 3, new graph = 4, quit = 5")
            chosen_function = int(input())

            if chosen_function == 1:

                print("Dijkstras algorithm:")

                dijkstra_result = algorithms.dijkstra(
                    testGraph, start_node, end_node)

                print("\nDijkstra path length from vertex ",
                      start_node, " to ", end_node, ": ", round(dijkstra_result[0].get(end_node), 1), sep="")
                print("Route from selfmade Dijkstra:", dijkstra_result[1])

                print(
                    "\nRoute and path length from NetworkX Dijkstra from", start_node, "to node", end_node, ":")
                print(nx.dijkstra_path(testGraph.nx_graph, start_node, end_node), "Length:", round((nx.dijkstra_path_length(
                    testGraph.nx_graph, start_node, end_node)), 1))

                nxf.visualize_nx_dijkstra(
                    testGraph.nx_graph, start_node, end_node)

            if chosen_function == 2:

                print("\nIDA*-algorithm:")

                ida_result = algorithms.ida_star(
                    testGraph, start_node, end_node)

                print("\nIDA* results for vertex ",
                      end_node, ": ", ida_result, sep="")

                nxf.visualize_nx_astar(
                    testGraph.nx_graph, start_node, end_node)

            if chosen_function == 3:
                print("Choose the indexes of start and end nodes:")
                print("Start node: ")
                start_node = input()
                start_node = int(start_node)
                print("End node: ")
                end_node = input()
                end_node = int(end_node)

            if chosen_function == 4:
                break
            if chosen_function == 5:
                print("\nThanks for using my program!")
                break
        if chosen_function == 5:
            break
