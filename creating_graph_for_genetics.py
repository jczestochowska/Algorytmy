import numpy as np
import pickle
import pandas
from Graph import *

graph_as_df = pandas.read_csv('graf_do_genetyki.csv',delimiter =' ')
graph_numpy = graph_as_df.as_matrix()

for edge in graph_numpy:
    edge[1] = edge[1] - 1
    edge[2] = edge[2] - 1

graph_numpy = graph_numpy[:,1:]

nodes = np.unique(graph_numpy)

g = Graph(False)

for i in range(len(nodes)):
    g.add_node()

for edge in graph_numpy:
    g.add_edge(edge[0],edge[1],1)

with open('genetics_graph_ready.pkl','wb') as file:
    pickle.dump(g,file)

