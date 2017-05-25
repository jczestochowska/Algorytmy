import graphviz as gv
from Graph import *

def greedy_coloring(graph):

    nodes_colors = [0] * len(graph.list_nodes)
    possible_colors = []

    for i in range(1,len(graph.list_nodes)+1):
        possible_colors.append(i)

    for node in graph.list_nodes:
        neighbours = graph.get_neighbours(node)
        neighbours_colors = [0] * len(graph.list_nodes)

        for neighbour in neighbours:
            neighbours_colors[neighbour] = nodes_colors[neighbour]

        for color in possible_colors:
            if color not in neighbours_colors:
                nodes_colors[node] = color
                break

    return nodes_colors

def graph_painting():

    g = gv.Graph(format='png')
    g1 = gv.Graph(format='png')
    g2 = gv.Graph(format='png')
    g3 = gv.Graph(format='png')
    g4 = gv.Graph(format='png')
    g5 = gv.Graph(format='png')

    g.node('0',color='green')
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

    g1.node('0',color='green')
    g1.node('1',color='blue')
    g1.node('2')
    g1.node('3')
    g1.node('4')
    g1.edge('0', '1', label="5")
    g1.edge('1', '4', label="4")
    g1.edge('4', '3', label="1")
    g1.edge('3', '1', label="3")
    g1.edge('1', '2', label="2")
    g1.edge('2', '3', label="3")
    g1.edge('2', '0', label="6")

    g2.node('0',color='green')
    g2.node('1',color='blue')
    g2.node('2')
    g2.node('3')
    g2.node('4',color='green')
    g2.edge('0', '1', label="5")
    g2.edge('1', '4', label="4")
    g2.edge('4', '3', label="1")
    g2.edge('3', '1', label="3")
    g2.edge('1', '2', label="2")
    g2.edge('2', '3', label="3")
    g2.edge('2', '0', label="6")


    g3.node('0',color='green')
    g3.node('1',color='blue')
    g3.node('2')
    g3.node('3',color='red')
    g3.node('4',color='green')
    g3.edge('0', '1', label="5")
    g3.edge('1', '4', label="4")
    g3.edge('4', '3', label="1")
    g3.edge('3', '1', label="3")
    g3.edge('1', '2', label="2")
    g3.edge('2', '3', label="3")
    g3.edge('2', '0', label="6")

    g4.node('0',color='green')
    g4.node('1',color='blue')
    g4.node('2',color='pink')
    g4.node('3',color='red')
    g4.node('4',color='green')
    g4.edge('0', '1', label="5")
    g4.edge('1', '4', label="4")
    g4.edge('4', '3', label="1")
    g4.edge('3', '1', label="3")
    g4.edge('1', '2', label="2")
    g4.edge('2', '3', label="3")
    g4.edge('2', '0', label="6")


    filename = g.render(filename='img_greedy/g',view=True)
    filename = g1.render(filename='img_greedy/g1',view=True)
    filename = g2.render(filename='img_greedy/g2',view=True)
    filename = g3.render(filename='img_greedy/g3',view=True)
    filename = g4.render(filename='img_greedy/g4',view=True)


if __name__ == '__main__':
    g = Graph(False)
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
    print(greedy_coloring(g))
    graph_painting()
