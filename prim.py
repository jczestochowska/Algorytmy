
from Algorytmy_repo.weight_matrix_numpy import *

def prim_algorithm(graph):

    sub_graph = Graph()
    sub_graph.weight_matrix = np.zeros(graph.weight_matrix.shape)
    added_edges = np.zeros(graph.weight_matrix.shape)
    added_edges[0][:] = graph.weight_matrix[0][:]
    added_nodes = {}
    for node in graph.list_nodes:
        added_nodes[node]=0
    added_nodes[0] = 1
    while sum(added_nodes.values()) != len(graph.list_nodes):
        minval = np.min(added_edges[np.nonzero(added_edges)])
        i = np.where(added_edges == minval)
        indx = i[1][0]
        if added_nodes[indx]==0:
                sub_graph.weight_matrix[i[0][0]][indx] = minval
                added_edges[indx][:] = graph.weight_matrix[indx][:]
                added_edges[i[0][0]][indx] = 0
                added_edges[indx][i[0][0]] = 0
                added_nodes[indx]=1

    return sub_graph.weight_matrix

if __name__ == '__main__':
    g=Graph()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_edge(3,4,2)
    g.add_edge(1,2,7)
    g.add_edge(1,3,3)
    g.add_edge(2,3,1)
    g.add_edge(1,4,4)
    g.add_edge(1,0,5)
    g.add_edge(0,2,6)
    print(g.weight_matrix)
    print('\n')
    print(prim_algorithm(g))