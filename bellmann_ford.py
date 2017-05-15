
from weight_matrix_numpy import *
import graphviz as gv

def bellmann_ford(graph, initial_node, final_node):

    weight_matrix = graph.weight_matrix
    list_nodes = graph.list_nodes
    previous = {}
    for node in list_nodes:
        previous[node] = node
    visited = []
    dijkstra_vector = np.full(len(list_nodes), np.inf)
    dijkstra_vector[initial_node] = 0
    current_node = initial_node

    for i in range(len(list_nodes)):

        if i == len(list_nodes) - 1:
            dijkstra_vector_copy = np.copy(dijkstra_vector)

        for node in range(len(weight_matrix[current_node, :])):
            if node not in visited and weight_matrix[current_node, node] != 0:
                if dijkstra_vector[current_node] + weight_matrix[current_node, node] < dijkstra_vector[node]:
                    dijkstra_vector[node] = dijkstra_vector[current_node] + weight_matrix[current_node, node]
                    previous[node] = current_node
        visited.append(current_node)
        d_v_copy = np.copy(dijkstra_vector)
        for node in visited:
            d_v_copy[node] = np.inf
        min_val_in_dijkstra_vec = np.min(d_v_copy[np.nonzero(d_v_copy)])
        current_node = np.where(d_v_copy == min_val_in_dijkstra_vec)[0][0]


        if i == len(list_nodes) - 1 and dijkstra_vector_copy != dijkstra_vector:
            print("there is a negative cycle")


    path = []
    path.append(final_node)
    path.append(previous[final_node])
    node = path[1]
    while initial_node not in path:
        previous_node = previous[node]
        path.append(previous_node)
        node = previous[previous_node]
    path.reverse()
    print(path)

def graph_colouring():
    g = gv.Graph(format='png')
    g1 = gv.Graph(format='png')
    g2 = gv.Graph(format='png')
    g3 = gv.Graph(format='png')
    g4 = gv.Graph(format='png')
    g5 = gv.Graph(format='png')

    g.node('0')
    g.node('1')
    g.node('2')
    g.node('3')
    g.node('4')
    g.edge('0', '1', label="-5")
    g.edge('1', '4', label="4")
    g.edge('4', '3', label="1")
    g.edge('3', '1', label="-3")
    g.edge('1', '2', label="2")
    g.edge('2', '3', label="3")
    g.edge('2', '0', label="6")

    g1.node('0',color="red")  #red - odwiedzone wierzcholki i curren nody blue - potencalne
    g1.node('1',color="blue")
    g1.node('2',color="blue")
    g1.node('3')
    g1.node('4')
    g1.edge('0', '1', label="-5",color="blue")
    g1.edge('1', '4', label="4")
    g1.edge('4', '3', label="1")
    g1.edge('3', '1', label="-3")
    g1.edge('1', '2', label="2")
    g1.edge('2', '3', label="3")
    g1.edge('2', '0', label="6",color="blue")

    g2.node('0',color="red")
    g2.node('1',color="red")
    g2.node('2',color="blue")
    g2.node('3',color="blue")
    g2.node('4',color="blue")
    g2.edge('0', '1',label="-5")
    g2.edge('1', '4', label="4",color="blue")
    g2.edge('4', '3', label="1")
    g2.edge('3', '1', label="-3",color="blue")
    g2.edge('1', '2', label="2",color="blue")
    g2.edge('2', '3', label="3")
    g2.edge('2', '0', label="6")

    g3.node('0',color="red")
    g3.node('1',color="red")
    g3.node('2')
    g3.node('3',color="red")
    g3.node('4')
    g3.edge('0', '1', label="-5")
    g3.edge('1', '4', label="4")
    g3.edge('4', '3', label="1")
    g3.edge('3', '1', label="-3")
    g3.edge('1', '2', label="2")
    g3.edge('2', '3', label="3")
    g3.edge('2', '0', label="6")

    g4.node('0',color="green")
    g4.node('1',color="green")
    g4.node('2')
    g4.node('3',color="green")
    g4.node('4')
    g4.edge('0', '1', label="-5",color="green")
    g4.edge('1', '4', label="4")
    g4.edge('4', '3', label="1")
    g4.edge('3', '1', label="-3",color="green")
    g4.edge('1', '2', label="2")
    g4.edge('2', '3', label="3")
    g4.edge('2', '0', label="6")
    #
    # g5.node('0',color="red")
    # g5.node('1',color="red")
    # g5.node('2',color="red")
    # g5.node('3',color="red")
    # g5.node('4')
    # g5.edge('0', '1', label="-5",color="green")
    # g5.edge('1', '4', label="4")
    # g5.edge('4', '3', label="1")
    # g5.edge('3', '1', label="-3",color="green")
    # g5.edge('1', '2', label="2")
    # g5.edge('2', '3', label="3")
    # g5.edge('2', '0', label="6")



    filename = g.render(filename='img_bellmann_ford/g',view=True)
    filename = g1.render(filename='img_bellmann_ford/g1',view=True)
    filename = g2.render(filename='img_bellmann_ford/g2',view=True)
    filename = g3.render(filename='img_bellmann_ford/g3',view=True)
    filename = g4.render(filename='img_bellmann_ford/g4',view=True)
    # filename = g5.render(filename='img_bellmann_ford/g5',view=True)

if __name__ == '__main__':
    g = Graph()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_edge(0, 1, -5)
    g.add_edge(1, 4, 4)
    g.add_edge(4, 3, 1)
    g.add_edge(3, 1, -3)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 0, 6)
    bellmann_ford(g, 0, 3)
    graph_colouring()