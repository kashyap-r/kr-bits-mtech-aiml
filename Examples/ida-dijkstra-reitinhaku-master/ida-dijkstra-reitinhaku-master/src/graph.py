import random
import networkx as nx
import netxfuncs as nxf
import math


class Graph:
    """Class for generating and modifying graphs.
    """

    def __init__(self, len_v):
        """Initializes the graph with an adjacency list filled with -1's representing the lack of
        an edge between two vertices.

        Args:
            len_v: The amount of vertices assigned to the created graph.
        """

        self.node_amount = len_v
        self.nodes = []
        self.edge = [[-1 for i in range(len_v)] for j in range(len_v)]
        self.seen = []
        self.nx_graph = nx.Graph()

    def add_generated_edge(self, start, end):
        """A method for adding edges between vertices. Edge weights are calculated from the positions of the nodes with
        the Euclidean distance formula.
        The start/end order doesn't matter since it's an undirected graph.

        Args:
            start: The first vertix to update.
            end: The second vertix to update.
            weight: Weight for the edge, calculated inside the method.
        """

        weight = math.sqrt(((self.nodes[end][0]-self.nodes[start][0])
                           ** 2 + (self.nodes[end][1] - self.nodes[start][1])**2))

        rounded_weight = round(weight, 1)
        self.edge[start][end] = rounded_weight
        self.edge[end][start] = rounded_weight

        self.nx_graph.add_edge(start, end, weight=rounded_weight)

    def generate_nodes(self, size):
        """A method for populating a random graph with this amount of nodes.
        Works the best with sizes between 5-20.
        """

        for i in range(size):
            if i == size:
                return

            xpos = random.randint(1, 100)
            ypos = random.randint(1, 100)

            self.nodes.append([xpos, ypos])

            self.nx_graph.add_node(i, pos=(xpos, ypos))

    def generate_edges(self, size):
        """A method for generating a random amount of edges between nodes.
        Visually works the best with sizes between 5-20, for algorithm testing use larger sizes.
        Chance for extra edges, "shortcuts", to appear can be modified.
        """

        for i in range(size):
            if i == size - 1:
                return
            chance = random.randint(0, 10)

            self.add_generated_edge(i, i+1)
            self.nx_graph.add_edge(i, i+1)

            # Chance for an shortcut between current and a random node to appear
            # Modify the for loop for more/less edges
            for k in range(2):
                if chance >= 1:
                    shortcut_node = random.randint(0, size - 1)
                    while shortcut_node == i:
                        shortcut_node = random.randint(0, size - 1)
                    self.add_generated_edge(i, shortcut_node)
                    self.nx_graph.add_edge(i, shortcut_node)
