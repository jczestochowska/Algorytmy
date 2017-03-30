
class Graph:
    def __init__(self):
        self.list_edges = []
        self.list_nodes=[]

    def add_edge(self,node1,node2,weight):
        self.list_edges.append([node1,node2,weight])

        for edge in self.list_edges:
            if edge[0] not in self.list_nodes:
                self.list_nodes.append(edge[0])
            elif edge[1] not in self.list_nodes:
                self.list_nodes.append(edge[1])
        self.buble_sort()
        return self

    def buble_sort(self):
        length = len(self.list_edges) - 1
        sorted = False
        while not sorted:
            sorted = True
            for element in range(0, length):
                if self.list_edges[element][2] < self.list_edges[element + 1][2]:
                    sorted = False
                    hold = self.list_edges[element + 1]
                    self.list_edges[element + 1] = self.list_edges[element]
                    self.list_edges[element] = hold
        return self

if __name__ == "__main__":
    g=Graph()
    g.add_edge('A','B',7)
    g.add_edge('B','C',2)
    g.add_edge('C','D',5)
    print(g.list_edges)
    print('\n')
    print(g.list_nodes)
