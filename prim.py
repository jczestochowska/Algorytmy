
from weight_matrix_numpy import *
import graphviz as gv

def prim_algorithm(graph):
    sub_graph = Graph()
    sub_graph.weight_matrix = np.zeros(graph.weight_matrix.shape)
    added_edges = np.zeros(graph.weight_matrix.shape)
    added_edges[0][:] = graph.weight_matrix[0][:]
    added_nodes = {}
    for node in graph.list_nodes:
        added_nodes[node] = 0
    added_nodes[0] = 1
    while sum(added_nodes.values()) != len(graph.list_nodes):
        minvalue_in_added_edges = np.min(added_edges[np.nonzero(added_edges)])
        minvalue_coordinates = np.where(added_edges == minvalue_in_added_edges)
        minvalue_y_coordinate = minvalue_coordinates[1][0]
        minvalue_x_coordinate = minvalue_coordinates[0][0]
        if added_nodes[minvalue_y_coordinate] == 0:
            sub_graph.weight_matrix[minvalue_coordinates[0][0]][minvalue_y_coordinate] = minvalue_in_added_edges
            added_edges[minvalue_y_coordinate] = graph.weight_matrix[minvalue_y_coordinate][:]
            added_edges[minvalue_x_coordinate][minvalue_y_coordinate] = 0
            added_edges[minvalue_y_coordinate][minvalue_x_coordinate] = 0
            added_nodes[minvalue_y_coordinate] = 1

    return sub_graph.weight_matrix

def graph_colouring(graph):

    g = gv.Graph(format='png')
    s_g1 = gv.Graph(format='png')
    s_g2 = gv.Graph(format='png')
    s_g3 = gv.Graph(format='png')
    s_g4 = gv.Graph(format='png')

    g.node('A')
    g.node('B')
    g.node('C')
    g.node('D')
    g.node('E')
    g.edge('D', 'E', label="1")
    g.edge('B', 'C', label="2")
    g.edge('B', 'D', label="3")
    g.edge('C', 'D', label="3")
    g.edge('B', 'E', label="4")
    g.edge('B', 'A', label="5")
    g.edge('A', 'C', label="6")
    #
    s_g1.node('A',color="red")
    s_g1.node('B',color="red")
    s_g1.node('C')
    s_g1.node('D')
    s_g1.node('E')
    s_g1.edge('D', 'E', label="1")
    s_g1.edge('B', 'C', label="2")
    s_g1.edge('B', 'D', label="3")
    s_g1.edge('C', 'D', label="3")
    s_g1.edge('B', 'E', label="4")
    s_g1.edge('B', 'A', label="5",color="red")
    s_g1.edge('A', 'C', label="6")

    s_g2.node('A',color="red")
    s_g2.node('B', color="red")
    s_g2.node('C', color="red")
    s_g2.node('D')
    s_g2.node('E')
    s_g2.edge('D', 'E',label="1")
    s_g2.edge('B', 'C', label="2", color="red")
    s_g2.edge('B', 'D', label="3")
    s_g2.edge('C', 'D', label="3")
    s_g2.edge('B', 'E', label="4")
    s_g2.edge('B', 'A', label="5",color="red")
    s_g2.edge('A', 'C', label="6")
    #
    s_g3.node('A',color="red")
    s_g3.node('B', color="red")
    s_g3.node('C', color="red")
    s_g3.node('D', color="red")
    s_g3.node('E')
    s_g3.edge('D', 'E', label="1")
    s_g3.edge('B', 'C', label="2",color="red")
    s_g3.edge('B', 'D', label="3",color="red")
    s_g3.edge('C', 'D', label="3")
    s_g3.edge('B', 'E', label="4")
    s_g3.edge('B', 'A', label="5",color="red")
    s_g3.edge('A', 'C', label="6")

    s_g4.node('A', color="red")
    s_g4.node('B', color="red")
    s_g4.node('C', color="red")
    s_g4.node('D', color="red")
    s_g4.node('E', color="red")
    s_g4.edge('D', 'E', label="1", color="red")
    s_g4.edge('B', 'C', label="2", color="red")
    s_g4.edge('B', 'D', label="3",color="red")
    s_g4.edge('C', 'D', label="3")
    s_g4.edge('B', 'E', label="4")
    s_g4.edge('B', 'A', label="5", color="red")
    s_g4.edge('A', 'C', label="6")

    filename = g.render(filename='img_prim/g')
    filename = s_g1.render(filename='img_prim/s_g1')
    filename = s_g2.render(filename='img_prim/s_g2')
    filename = s_g3.render(filename='img_prim/s_g3')
    filename = s_g4.render(filename='img_prim/s_g4')

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
    print(g.weight_matrix)
    print('\n')
    print(prim_algorithm(g))
    graph_colouring(g)
