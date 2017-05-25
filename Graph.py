#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class Graph:
    def __init__(self,directed):
        self.weight_matrix = np.zeros(shape =(0,0))
        self.list_nodes = []
        self.directed = directed

    def add_node(self):
        zero= np.zeros(shape=(1,self.weight_matrix.shape[0]))
        self.weight_matrix = np.vstack([self.weight_matrix, zero])
        zero2= np.zeros(shape=(self.weight_matrix.shape[0], 1))
        self.weight_matrix = np.hstack([self.weight_matrix, zero2])
        return self

    def add_edge(self,node1,node2,weight):

        if self.directed == False:
            self.weight_matrix[node1][node2] = weight
            self.weight_matrix[node2][node1] = weight
            if node1 not in self.list_nodes:
                self.list_nodes.append(node1)
            if node2 not in self.list_nodes:
                self.list_nodes.append(node2)
        else:
            self.weight_matrix[node1][node2] = weight
            if node1 not in self.list_nodes:
                self.list_nodes.append(node1)
            if node2 not in self.list_nodes:
                self.list_nodes.append(node2)
        return self

    def increase_flow(self, increaser, node1, node2):
        self.weight_matrix[node1, node2] += increaser
        return self

    def decrease_flow(self, decreaser, node1, node2):
        self.weight_matrix[node1, node2] -= decreaser
        return self

    def edge_exists(self, node1, node2):
        if self.weight_matrix[node1, node2] == 0:
            return False
        else:
            return True

    def path_exists(self, source, sink):

        visited,path = self.finding_paths(source)
        if visited[sink] == True:
            return True
        else:
            return False

    def finding_paths(self, source):

        path = [-1] * len(self.weight_matrix)
        queue = []
        visited = [False] * len(self.weight_matrix)

        queue.append(source)

        while queue:
            current = queue.pop(0)
            for node, weight in enumerate(self.weight_matrix[current]):
                if visited[node] == False and weight != 0:
                    visited[node] = True
                    path[node] = current
                    queue.append(node)

        return visited,path

    def find_paths_smallest_capacity(self, source, sink, parent):
        node = sink
        smallest_capacity = float('Inf')
        while node != source:
            node_flow = self.weight_matrix[parent[node], [node]]
            smallest_capacity = min(smallest_capacity, node_flow)
            node = parent[node]

        return smallest_capacity

    def get_neighbours(self,node):

        nodes_edges = self.weight_matrix[node]
        neighbours = np.where(nodes_edges != 0)[0]
        return neighbours

if __name__ == '__main__':
    g = Graph(True)
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_edge(0, 1, 5)
    g.add_edge(1, 4, 4)
    g.add_edge(4, 3, 1)
    g.add_edge(3, 1, 3)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 0, 6)
    print(g.get_neighbours(2))
    print(g.weight_matrix)