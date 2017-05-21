from weight_matrix_numpy import *
import graphviz as gv

def ford_fulkerson(graph,source,sink):

    max_flow = 0

    while graph.path_exists(source, sink):

        parents = finding_path(graph, source)
        smallest_capacity = find_smallest_capacity(graph, source, sink, parents)
        max_flow += smallest_capacity
        current_node = sink

        while current_node != source:

            parent = getparent(current_node,parents)

            if graph.edge_exists(parent,current_node):
                graph.decrease_flow(smallest_capacity,parent,current_node,)
                graph.increase_flow(smallest_capacity,current_node,parent)

            current_node = parents[current_node]

    print("Maximum flow is: %d" %max_flow)

    return max_flow


def getparent(current_node,parents):
    parent = parents[current_node]
    return parent

def finding_path (graph, source):

    path = [-1] * len(graph.weight_matrix)
    queue = []
    visited = [False] * len(graph.weight_matrix)

    queue.append(source)

    while queue:
        current = queue.pop(0)
        for node, weight in enumerate(graph.weight_matrix[current]):
            if visited[node] == False and weight != 0:
                visited[node] = True
                path[node] = current
                queue.append(node)

    return path

def find_smallest_capacity(graph, source, sink, parent):
    node = sink
    smallest_capacity = float('Inf')
    while node != source:
        node_flow = graph.weight_matrix[parent[node], [node]]
        smallest_capacity = min(smallest_capacity, node_flow)
        node = parent[node]

    return smallest_capacity

def graph_colouring():

    g = gv.Digraph(format='png')
    g1 = gv.Digraph(format='png')
    g2 = gv.Digraph(format='png')
    g3 = gv.Digraph(format='png')
    g4 = gv.Digraph(format='png')
    g5 = gv.Digraph(format='png')

    g.node('0')
    g.node('1')
    g.node('2')
    g.node('3')
    g.node('4')
    g.edge('0', '1', label="5")
    g.edge('1', '4', label="4")
    g.edge('4', '3', label="1")
    g.edge('3', '1', label="3")
    g.edge('1', '2', label="2")
    g.edge('2', '3', label="3")
    g.edge('2', '0', label="6")

    g1.node('0')
    g1.node('1')
    g1.node('2')
    g1.node('3')
    g1.node('4')
    g1.edge('0', '1', label="3",color = 'green')
    g1.edge('1', '4', label="4")
    g1.edge('4', '3', label="1")
    g1.edge('3', '1', label="3")
    g1.edge('2', '3', label="1",color='green')
    g1.edge('2', '0', label="6")
    g1.edge('3', '2', label="2",color = 'red')

    g2.node('0')
    g2.node('1')
    g2.node('2')
    g2.node('3')
    g2.node('4')
    g2.edge('0', '1', label="2", color='green')
    g2.edge('1', '4', label="3",color='green')
    g2.edge('3', '1', label="3")
    g2.edge('2', '3', label="1")
    g2.edge('2', '0', label="6")
    g2.edge('3', '2', label="2")
    g2.edge('4', '1', label="1",color='red')
    g2.edge('1', '0', label="1", color='red')


    g3.node('0')
    g3.node('1')
    g3.node('2')
    g3.node('3')
    g3.node('4')
    g3.edge('0', '1', label="4", color='green')
    g3.edge('1', '4', label="3",color='green')
    g3.edge('3', '1', label="3")
    g3.edge('1', '2', label="2")
    g3.edge('2', '3', label="1")
    g3.edge('2', '0', label="6")
    g3.edge('3', '2', label="2")
    g3.edge('4', '1', label="1",color='red')
    g3.edge('1', '0', label="1", color='red')


    filename = g.render(filename='img_ford_fulkerson/g',view=True)
    filename = g1.render(filename='img_ford_fulkerson/g1',view=True)
    filename = g2.render(filename='img_ford_fulkerson/g2',view=True)

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
    graph_colouring()
    ford_fulkerson(g,0,3)
