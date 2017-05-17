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




if __name__ == '__main__':
    g = Graph()
    g.add_node()
    g.add_node()
    g.add_edge(0,1,2)
    print(g.weight_matrix)