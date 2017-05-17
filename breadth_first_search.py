
def breadth_first_search(graph, source, sink):
    parent = [-1] * len(graph.weight_matrix)
    queue = []
    visited = [False] * len(graph.weight_matrix)

    queue.append(source)

    while queue:
        current = queue.pop(0)
        for node, weight in enumerate(graph.weight_matrix[current]):
            if visited[node] == False and weight != 0:
                visited[node] = True
                parent[node] = current
                queue.append(node)

    if visited[sink] == True:
        condition = True
    else:
        condition = False


    return condition, parent