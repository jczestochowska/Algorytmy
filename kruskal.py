#!/usr/bin/env python
# -*- coding: utf-8 -*-


from list_edges_simple import *


def kruskal_algorithm(graph):

    # lista zbiorow z ktorych kazdy zbior to osobne drzewo
    forest = []
    sub_graph = Graph()
    for node in graph.list_nodes:
        forest.append(set([node]))
    while graph.list_edges:
        edge = graph.list_edges.pop()
        node1 = set(edge[0])
        node2 = set(edge[1])
        for tree in forest:
            if node1.issubset(tree):
                indx1 = forest.index(tree)
            if node2.issubset(tree):
                indx2 = forest.index(tree)
        if indx1 != indx2:
            forest[indx1].update(forest[indx2])
            forest.remove(forest[indx2])
            sub_graph.list_edges.append(edge)
    return sub_graph


if __name__ == "__main__":
    g = Graph()
    g.add_edge('D','E',1)
    g.add_edge('B','C',2)
    g.add_edge('B','D',3)
    g.add_edge('C','D',3)
    g.add_edge('B','E',4)
    g.add_edge('B','A',5)
    g.add_edge('A','C',6)
    print(g.list_edges)
    print('\n')
    print(kruskal_algorithm(g).list_edges)


