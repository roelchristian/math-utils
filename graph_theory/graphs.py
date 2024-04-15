## Utility for working with graphs

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Graph():
    def __init__(self, graph_type='undirected', vertices=None, edges=None):
        self.graph = self.create_graph(graph_type, vertices, edges)

    def create_graph(self, graph_type, vertices, edges):
        if graph_type == 'directed':
            graph = nx.DiGraph()
        
        elif graph_type == 'undirected':
            graph = nx.Graph()
       
        else:
            raise ValueError("Invalid graph type. Must be 'directed' or 'undirected'")

        if vertices:
            graph.add_nodes_from(vertices)

        if edges:
            graph.add_edges_from(edges)

        return graph

    def draw_graph(self, save=False, filename=None):
        nx.draw(self.graph, with_labels=True, font_weight='bold')
        if save:
            if filename:
                plt.savefig(filename)
            else:
                raise ValueError("Please provide a filename to save the graph")
        plt.show()

    def degree_centrality(self):
        return nx.degree_centrality(self.graph)

    def closeness_centrality(self):
        return nx.closeness_centrality(self.graph)

    def betweenness_centrality(self):
        return nx.betweenness_centrality(self.graph)

    def eigenvector_centrality(self):
        return nx.eigenvector_centrality(self.graph)

    def pagerank(self):
        return nx.pagerank(self.graph)

    def clustering_coefficient(self):
        return nx.clustering(self.graph)

    def shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source=source, target=target)

    def shortest_path_length(self, source, target):
        return nx.shortest_path_length(self.graph, source=source, target=target)

    def connected_components(self):
        return nx.connected_components(self.graph)

    def connected_component_subgraphs(self):
        return nx.connected_component_subgraphs(self.graph)

    def minimum_spanning_tree(self):
        return nx.minimum_spanning_tree(self.graph)

    def maximum_flow(self, source, target):
        return nx.maximum_flow(self.graph, source=source, target=target)

    def minimum_cut(self, source, target):
        return nx.minimum_cut(self.graph, source=source, target=target)

    def all_pairs_shortest_path(self):
        return dict(nx.all_pairs_shortest_path(self.graph))

    def all_pairs_shortest_path_length(self):
        return dict(nx.all_pairs_shortest_path_length(self.graph))

    def all_pairs_node_connectivity(self):
        return nx.all_pairs_node_connectivity(self.graph)

    def all_pairs_edge_connectivity(self):
        return nx.all_pairs_edge_connectivity(self.graph)

    def is_connected(self):
        return nx.is_connected(self.graph)

    def is_strongly_connected(self):
        return nx.is_strongly_connected(self.graph)

    def is_weakly_connected(self):
        return nx.is_weakly_connected(self.graph)

    def is_biconnected(self):
        return nx.is_biconnected(self.graph)

    def is_regular(self):
        return nx.is_regular(self.graph)
    
def main():
    vertices = ["A", "B", "C", "D", "E"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    graph_type = 'undirected'
    graph = Graph(graph_type, vertices, edges)

    graph.draw_graph(save=True, filename='graph.png')

if __name__ == '__main__':
    main()