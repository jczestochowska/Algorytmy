#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Graph:

    def __init__(self, weight_matrix):
        if not weight_matrix:
            self.list_neighbours = {}
        else:
            self.list_neighbours = weight_matrix


    def add_node(self, new_node):
        self.list_neighbours[new_node] = []


    def add_edge(self, weight, start, end, directed):

        start_dictvalue = self.list_neighbours[start]
        end_dictvalue = self.list_neighbours[end]
        if directed is True:
            start_dictvalue.append((end,weight))
            self.list_neighbours[start] = start_dictvalue
        else:
            start_dictvalue.append((end,weight))
            end_dictvalue.append((start,weight))


    def add_neighbour(self, weight, start, end, directed):

        self.add_node(end)
        self.add_edge(weight,start,end,directed)


    def print_graph(self):
        print(self.list_neighbours.items())


    #
    def remove_edge(self, start, end, directed):
        if directed is True:
            self.list_neighbours[start] = []
        else:
            self.list_neighbours[start] = []
            self.list_neighbours[end] = []


if __name__ == "__main__":

    graph = Graph(None)
    graph.add_node('B')
    graph.add_node('A')
    graph.print_graph()
    graph.add_edge(5,'A','B',False)
    print('\n')
    graph.print_graph()
    graph.add_neighbour(7,'B','C',False)
    print('\n')
    graph.print_graph()

