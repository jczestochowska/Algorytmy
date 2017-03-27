#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Graph:

    def __init__(self):
            self.list_neighbours = {}


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



    def remove_node(self,start):
            del self.list_neighbours[start]
            list_values = self.list_neighbours.values()
            for value in list_values:
                index = 0;
                temp_range = len(value)
                for i in range(temp_range):
                    if value[index][0] == start:
                        value.remove(value[index])
                        i += 1
                    else:
                        i += 1
                        index += 1

    def remove_edge(self,start,end,directed):
        if directed is True:
            list_values = self.list_neighbours.values()
            for value in list_values:
                index = 0;
                temp_range = len(value)
                for i in range(temp_range):
                    if value[index][0] == start:
                        value.remove(value[index])
                        i += 1
                    else:
                        i += 1
                        index += 1
        else:
            list_values = self.list_neighbours.values()
            for value in list_values:
                index = 0;
                temp_range = len(value)
                for i in range(temp_range):
                    if value[index][0] == start:
                        value.remove(value[index])
                        i += 1
                    else:
                        i += 1
                        index += 1
            list_values = self.list_neighbours.values()
            for value in list_values:
                index = 0;
                temp_range = len(value)
                for i in range(temp_range):
                    if value[index][0] == end:
                        value.remove(value[index])
                        i += 1
                    else:
                        i += 1
                        index += 1



if __name__ == "__main__":
    graph = Graph()
    graph.add_node('B')
    graph.add_node('A')
    graph.print_graph()
    graph.add_edge(5,'A','B',False)
    print('\n')
    graph.print_graph()
    graph.add_neighbour(7,'B','C',False)
    print('\n')
    graph.print_graph()
    print('\n')
    graph.add_edge(2,'C','A',False)
    graph.print_graph()
    print('\n')
    graph.remove_node('A')
    graph.print_graph()
    graph.remove_edge('B','C', False)
    print('\n')
    graph.print_graph()
