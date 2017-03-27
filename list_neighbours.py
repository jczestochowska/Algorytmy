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
                index = 0
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
                index = 0
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
                index = 0
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
                index = 0
                temp_range = len(value)
                for i in range(temp_range):
                    if value[index][0] == end:
                        value.remove(value[index])
                        i += 1
                    else:
                        i += 1
                        index += 1

    def nodes_number(self):
        print(len(self.list_neighbours))
        return len(self.list_neighbours)


    def neighbours_and_edges_number(self,node):
        count = 0
        for key in self.list_neighbours.keys():
            if key == node and self.list_neighbours[key]:
                count += 1
        for value in self.list_neighbours.values():
            temp_index = len(value)-1
            for i in range(len(value)):
                if value[i][0] == node:
                    count += 1
        print(count)
        return count


if __name__ == "__main__":
    graph = Graph()
    graph.add_node('B')
    graph.add_node('A')
    graph.print_graph()
    graph.add_edge(5,'A','B',True)
    print('\n')
    graph.print_graph()
    graph.add_neighbour(7,'B','C',True)
    print('\n')
    graph.print_graph()
    print('\n')
    graph.add_edge(2,'C','A',True)
    graph.print_graph()
    print('\n')
    # graph.remove_node('A')
    # graph.print_graph()
    # graph.remove_edge('B','C', False)
    # print('\n')
    # graph.print_graph()
    graph.neighbours_and_edges_number('B')
