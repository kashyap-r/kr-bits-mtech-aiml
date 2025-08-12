import matplotlib.pyplot as plt
import networkx as nx


def visualize_nx_dijkstra(graph, start, end):
    """Method for visualizing the graph using Networkx, used only for visualization
    and result-comparision purposes.

    Args:
        graph: Gets the dict of dicts form of the graph as input and 
        visualizes it to a graph using (mostly) Networkx's built-in graph tools.
    """

    plt.figure(figsize=(12, 10))

    pos = nx.get_node_attributes(graph, 'pos')

    nx.draw(graph, pos, node_color='k')

    path = nx.dijkstra_path(graph, start, end)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges,
                           edge_color='r', width=10)

    nx.draw_networkx_nodes(graph, pos, node_size=500)

    nx.draw_networkx_labels(graph, pos, font_size=12, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")

    plt.show()


def visualize_nx_astar(graph, start, end):
    """Method for visualizing the graph using Networkx, used only for visualization
    and result-comparision purposes.

    Args:
        graph (_type_): Gets the dict of dicts form of the graph as input and 
        visualizes it to a graph using (mostly) Networkx's built-in graph tools.
    """

    plt.figure(figsize=(12, 10))

    pos = nx.get_node_attributes(graph, 'pos')

    nx.draw(graph, pos, node_color='k')

    path = nx.astar_path(graph, start, end)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges,
                           edge_color='r', width=10)

    nx.draw_networkx_nodes(graph, pos, node_size=500)

    nx.draw_networkx_labels(graph, pos, font_size=12, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")

    plt.show()
