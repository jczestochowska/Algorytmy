from weight_matrix_numpy import *
from breadth_first_search import *

def ford_fulkerson(graph,source,sink):

    max_flow = 0

    while breadth_first_search(graph,source,sink)[0]:

        parent = breadth_first_search(graph,source,sink)[1]
        smallest_capacity = float('Inf')
        path = []
        node = sink


        while node != source:
            node_flow = graph.weight_matrix[parent[node],[node]]
            smallest_capacity = min(smallest_capacity,node_flow)
            node = parent[node]
        max_flow += smallest_capacity
        node = sink
        while node != source:
            graph.weight_matrix[parent[node]][node] -= smallest_capacity
            graph.weight_matrix[node][parent[node]] += smallest_capacity
            node = parent[node]
    print("Maximum flow is: %d" %(max_flow))
    return max_flow





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
    ford_fulkerson(g,0,3)