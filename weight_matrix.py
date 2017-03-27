#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Graph:
    def __init__(self):
        self.weight_matrix= [[]]

    def add_node(self):
        if self.weight_matrix == [[]]:
            for row in self.weight_matrix:
                row.append(0)
        else:
            for row in self.weight_matrix:
                row.append(0)
            self.weight_matrix.append(self.zerolistmaker(len(row)))

    def add_edge(self,weight,directed,start,end):
        if directed is True:
            self.weight_matrix[start][end] = weight
        elif start == end and directed is False:
            print("non-directed graph has no loops")
        else:
            self.weight_matrix[start][end] = weight
            self.weight_matrix[end][start] = weight


    def add_neighbour(self,weight,directed,start):
        self.add_node()
        end = len(self.weight_matrix)-1
        self.add_edge(weight,directed,start,end)

    def zerolistmaker(self,n):
        listofzeros = [0] * n
        return listofzeros

    def remove_edge(self,start,end,directed):
        if directed is True:
            self.weight_matrix[start][end] = 0
        else:
            self.weight_matrix[start][end] = 0
            self.weight_matrix[end][start] = 0

    def remove_node(self, node):
        del self.weight_matrix[node]
        for item in self.weight_matrix:
            del item[node]

    def neigbours_and_edges_number(self,node):
        count = 0;
        for item in self.weight_matrix[node]:
            if item != 0:
                count += 1
        print(count)
        return count

    def node_number(self):
        print(len(self.weight_matrix))
        return len(self.weight_matrix)



if __name__ == '__main__':

    graph = Graph()
    graph.add_node()
    print('\n')
    print(graph.weight_matrix)
    graph.add_node()
    print('\n')
    print(graph.weight_matrix)
    graph.add_neighbour(4,False,0)
    print('\n')
    print(graph.weight_matrix)
    graph.add_edge(3,False,1,1)
    print('\n')
    print(graph.weight_matrix)
    graph.remove_edge(0,2,True)
    print('\n')
    print(graph.weight_matrix)
    graph.remove_node(0)
    print('\n')
    print(graph.weight_matrix)
    graph.neigbours_and_edges_number(0)