
import unittest
import algorithms
from graph import Graph
import networkx


class TestingGraph(unittest.TestCase):

    def setUp(self):
        self.testing_graph = Graph(5)
        self.testing_graph_long = Graph(7)

    def test_generated_graph_dijkstra(self):
        generated_graph = Graph(50)

        generated_graph.generate_nodes(50)
        generated_graph.generate_edges(50)

        dijkstra_result = algorithms.dijkstra(generated_graph, 0, 49)
        nx_result = networkx.dijkstra_path_length(
            generated_graph.nx_graph, 0, 49)

        self.assertEqual(dijkstra_result[0].get(49),
                         nx_result)

    def test_generated_graph_idastar(self):
        generated_graph = Graph(50)

        generated_graph.generate_nodes(30)
        generated_graph.generate_edges(30)

        idastar_result = algorithms.ida_star(generated_graph, 0, 29)
        nx_result = networkx.astar_path_length(
            generated_graph.nx_graph, 0, 29)

        self.assertEqual(idastar_result,
                         nx_result)

    def test_generated_dijkstra_route(self):
        generated_graph = Graph(50)

        generated_graph.generate_nodes(50)
        generated_graph.generate_edges(50)

        dijkstra_result = algorithms.dijkstra(generated_graph, 0, 49)
        nx_result = networkx.dijkstra_path(generated_graph.nx_graph, 0, 49)

        self.assertEqual(dijkstra_result[1],
                         nx_result)


if __name__ == '__main__':
    unittest.main()
