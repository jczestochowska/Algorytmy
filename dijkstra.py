#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weight_matrix_numpy import *

def dijkstra(graph,initial_node, final_node):

    weight_matrix = graph.weight_matrix
    list_nodes = graph.list_nodes
    previous = {}
    for node in list_nodes:
        previous[node] = node
    visited = []
    dijkstra_vector = np.full(len(list_nodes),np.inf)
    dijkstra_vector[initial_node] = 0
    current_node = initial_node

    while final_node not in visited:

        for node in range(len(weight_matrix[current_node,:])):
            if node not in visited and weight_matrix[current_node, node] != 0:
                if dijkstra_vector[current_node]+weight_matrix[current_node,node]<dijkstra_vector[node]:
                    dijkstra_vector[node] = dijkstra_vector[current_node]+weight_matrix[current_node,node]
                    previous[node] = current_node
        visited.append(current_node)
        d_v_copy = np.copy(dijkstra_vector)
        for node in visited:
            d_v_copy[node] = np.inf
        min_val_in_dijkstra_vec = np.min(d_v_copy[np.nonzero(d_v_copy)])
        current_node = np.where(d_v_copy == min_val_in_dijkstra_vec)[0][0]

    path=[]
    path.append(final_node)
    path.append(previous[final_node])
    node = path[1]
    while initial_node not in path:
        previous_node = previous[node]
        path.append(previous_node)
        node = previous[previous_node]
    path.reverse()
    print(path)


if __name__ == '__main__':
    g = Graph()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_edge(0,1,5)
    g.add_edge(1,4,4)
    g.add_edge(4,3,1)
    g.add_edge(3,1,3)
    g.add_edge(1,2,2)
    g.add_edge(2,3,3)
    g.add_edge(2,0,6)
    dijkstra(g,0,3)