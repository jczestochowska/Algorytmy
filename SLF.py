import graphviz as gv
from Graph import *

def SLF(graph):
    nodes_colors = [0] * len(graph.list_nodes)
    possible_colors = []
    nodes_degrees = [0] * len(graph.list_nodes)

    for i in range(1,len(graph.list_nodes)+1):
        possible_colors.append(i)

    for node in graph.list_nodes:
        neighbours = graph.get_neighbours(node)
        nodes_degrees[node] = len(neighbours)

    while not all(nodes_colors):
        nodes_saturation = [0] * len(graph.list_nodes)
        neighbours_colors = [0] * len(graph.list_nodes)

        for node in graph.list_nodes:
            neighbours = graph.get_neighbours(node)
            for neighbour in neighbours:
                    neighbours_colors[neighbour] = nodes_colors[neighbour]
            neighbours_colors=set(neighbours_colors)
            if neighbours_colors == set([0]):
                nodes_saturation[node] = 0
            elif 0 in neighbours_colors:
                nodes_saturation[node] = len(neighbours_colors)-1
            else:
                nodes_saturation[node] = len(neighbours_colors)

            neighbours_colors = [0] * len(graph.list_nodes)

        greatest_saturation = max(nodes_saturation)
        nodes_max_saturated = [i for i in range(len(nodes_saturation)) if nodes_saturation[i] == greatest_saturation]

        choosing_node = [0] * len(graph.list_nodes)
        for node in nodes_max_saturated: choosing_node[node] = nodes_degrees[node]

        node = choosing_node.index(max(choosing_node))
        nodes_degrees[node] = 0
        # kolorowanie zachłanne
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

    g.node('0')
    g.node('1',color='green')
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
    g1.node('1',color='green')
    g1.node('2',color='blue')
    g1.node('3')
    g1.node('4')
    g1.edge('0', '1', label="5")
    g1.edge('1', '4', label="4")
    g1.edge('4', '3', label="1")
    g1.edge('3', '1', label="3")
    g1.edge('1', '2', label="2")
    g1.edge('2', '3', label="3")
    g1.edge('2', '0', label="6")

    g2.node('0')
    g2.node('1',color='green')
    g2.node('2',color='blue')
    g2.node('3',color='red')
    g2.node('4')
    g2.edge('0', '1', label="5")
    g2.edge('1', '4', label="4")
    g2.edge('4', '3', label="1")
    g2.edge('3', '1', label="3")
    g2.edge('1', '2', label="2")
    g2.edge('2', '3', label="3")
    g2.edge('2', '0', label="6")


    g3.node('0',color='red')
    g3.node('1',color='green')
    g3.node('2',color='blue')
    g3.node('3',color='red')
    g3.node('4')
    g3.edge('0', '1', label="5")
    g3.edge('1', '4', label="4")
    g3.edge('4', '3', label="1")
    g3.edge('3', '1', label="3")
    g3.edge('1', '2', label="2")
    g3.edge('2', '3', label="3")
    g3.edge('2', '0', label="6")

    g4.node('0',color='red')
    g4.node('1',color='green')
    g4.node('2',color='blue')
    g4.node('3',color='red')
    g4.node('4',color='blue')
    g4.edge('0', '1', label="5")
    g4.edge('1', '4', label="4")
    g4.edge('4', '3', label="1")
    g4.edge('3', '1', label="3")
    g4.edge('1', '2', label="2")
    g4.edge('2', '3', label="3")
    g4.edge('2', '0', label="6")


    filename = g.render(filename='img_SLF/g',view=True)
    filename = g1.render(filename='img_SLF/g1',view=True)
    filename = g2.render(filename='img_SLF/g2',view=True)
    filename = g3.render(filename='img_SLF/g3',view=True)
    filename = g4.render(filename='img_SLF/g4',view=True)

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
    print(SLF(g))
    graph_painting()