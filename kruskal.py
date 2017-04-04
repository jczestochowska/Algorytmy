#!/usr/bin/env python
# -*- coding: utf-8 -*-


from list_edges_simple import *
import graphviz as gv


def kruskal_algorithm(graph):

    # lista zbiorow z ktorych kazdy zbior to osobne drzewo
    forest = []
    sub_graph = Graph()
    iterations_count = 0
    for node in graph.list_nodes:
        forest.append(set([node]))

    while graph.list_edges:
        edge = graph.list_edges.pop()
        node1 = set(edge[0])
        node2 = set(edge[1])
        iterations_count += 1
        for tree in forest:
            if node1.issubset(tree):
                indx1 = forest.index(tree)
            if node2.issubset(tree):
                indx2 = forest.index(tree)
        if indx1 != indx2:
            forest[indx1].update(forest[indx2])
            forest.remove(forest[indx2])
            sub_graph.list_edges.append(edge)

    for edge in sub_graph.list_edges:
        if edge[0] not in sub_graph.list_nodes:
            sub_graph.list_nodes.append(edge[0])
        elif edge[1] not in sub_graph.list_nodes:
            sub_graph.list_nodes.append(edge[1])

    print(sub_graph.list_edges)
    print(sub_graph.list_nodes)

    return sub_graph

def graph_colouring(graph):

    g = gv.Graph(format ='png')
    s_g1 = gv.Graph(format='png')
    s_g2 = gv.Graph(format='png')
    s_g3 = gv.Graph(format='png')
    s_g4 = gv.Graph(format='png')

    g.node('A')
    g.node('B')
    g.node('C')
    g.node('D')
    g.node('E')
    g.edge('D','E',label = "1")
    g.edge('B','C',label = "2")
    g.edge('B','D',label = "3")
    g.edge('C','D',label = "3")
    g.edge('B','E',label = "4")
    g.edge('B','A',label = "5")
    g.edge('A','C',label = "6")
    #
    s_g1.node('A')
    s_g1.node('B')
    s_g1.node('C')
    s_g1.node('D',color="red")
    s_g1.node('E',color="red")
    s_g1.edge('D','E',label = "1",color="red")
    s_g1.edge('B','C',label = "2")
    s_g1.edge('B','D',label = "3")
    s_g1.edge('C','D',label = "3")
    s_g1.edge('B','E',label = "4")
    s_g1.edge('B','A',label = "5")
    s_g1.edge('A','C',label = "6")

    s_g2.node('A')
    s_g2.node('B',color="blue")
    s_g2.node('C',color="blue")
    s_g2.node('D',color="red")
    s_g2.node('E',color="red")
    s_g2.edge('D','E',label = "1",color="red")
    s_g2.edge('B','C',label = "2",color="blue")
    s_g2.edge('B','D',label = "3")
    s_g2.edge('C','D',label = "3")
    s_g2.edge('B','E',label = "4")
    s_g2.edge('B','A',label = "5")
    s_g2.edge('A','C',label = "6")
    #
    s_g3.node('A')
    s_g3.node('B',color="red")
    s_g3.node('C',color="red")
    s_g3.node('D',color="red")
    s_g3.node('E',color="red")
    s_g3.edge('D','E',label = "1",color="red")
    s_g3.edge('B','C',label = "2",color="red")
    s_g3.edge('B','D',label = "3")
    s_g3.edge('C','D',label = "3",color="red")
    s_g3.edge('B','E',label = "4")
    s_g3.edge('B','A',label = "5")
    s_g3.edge('A','C',label = "6")

    s_g4.node('A',color="red")
    s_g4.node('B',color="red")
    s_g4.node('C',color="red")
    s_g4.node('D',color="red")
    s_g4.node('E',color="red")
    s_g4.edge('D','E',label = "1",color="red")
    s_g4.edge('B','C',label = "2",color="red")
    s_g4.edge('B','D',label = "3")
    s_g4.edge('C','D',label = "3",color="red")
    s_g4.edge('B','E',label = "4")
    s_g4.edge('B','A',label = "5",color="red")
    s_g4.edge('A','C',label = "6")



    filename = g.render(filename='img_kruskal/g')
    filename = s_g1.render(filename='img_kruskal/s_g1')
    filename = s_g2.render(filename='img_kruskal/s_g2')
    filename = s_g3.render(filename='img_kruskal/s_g3')
    filename = s_g4.render(filename='img_kruskal/s_g4')


if __name__ == "__main__":
    g = Graph()
    g.add_edge('D','E',1)
    g.add_edge('B','C',2)
    g.add_edge('B','D',3)
    g.add_edge('C','D',3)
    g.add_edge('B','E',4)
    g.add_edge('B','A',5)
    g.add_edge('A','C',6)
    # g =gv.Graph(format ='png')
    # g.node('A')
    # g.node('B')
    # g.node('C')
    # g.node('D')
    # g.node('E')
    # g.edge('D','E',label = "1")
    # g.edge('B','C',label = "2")
    # g.edge('B','D',label = "3")
    # g.edge('C','D',label = "3")
    # g.edge('B','E',label = "4")
    # g.edge('B','A',label = "5")
    # g.edge('A','C',label = "6")
    # print(g.source)
    # filename = g.render(filename='img/g')
    # print(g.list_edges)
    # print('\n')
    kruskal_algorithm(g)
    # print (filename)
    graph_colouring(g)
