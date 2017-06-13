import random
import numpy
import pickle
import graphviz as gv
import pandas

def graph_painting():

    with open('best_individual.pkl','rb') as file:
        best_individual = pickle.load(file)

    with open('genetics_graph_ready.pkl','rb') as file:
        graph_before_genetics = pickle.load(file)


    graph_draw = gv.Graph(format='png')
    nodes = sorted(graph_before_genetics.list_nodes)

    for node in nodes:
        node = str(node)
        graph_draw.node(node)

    graph_as_df = pandas.read_csv('graf_do_genetyki.csv', delimiter=' ')
    graph_numpy = graph_as_df.as_matrix()

    for edge in graph_numpy:
        edge[1] = edge[1] - 1
        edge[2] = edge[2] - 1
        start = str(edge[1])
        stop = str(edge[2])
        graph_draw.edge(start, stop)


    filename = graph_draw.render(filename='img_after_genetic/g',view=True)

graph_painting()
