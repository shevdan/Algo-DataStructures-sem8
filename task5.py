from abc import abstractproperty


class Edge:
    def __init__(self, v1, v2, weight) -> None:
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    
    def __str__(self):
        return f"{self.v1}, {self.v2}, {self.weight}"

    def __eq__(self, other):
        return self.v1 == other.v1 and self.v2 == other.v2 and self.weight == other.weight


def dfs(graph: dict, vertex: int, visited: list):
    if vertex not in visited:
        visited.append(vertex)
        for adjacent in graph[vertex]:
            dfs(graph, adjacent, visited)

def solve(edge: Edge, graph, lst_edges: list):
    new_graph = graph
    for curr_edge in lst_edges:
        if curr_edge == edge:
            continue
        if curr_edge.weight > edge.weight:
            try:
                new_graph[curr_edge.v1].remove(curr_edge.v2)
            except:
                pass
            try:
                new_graph[curr_edge.v2].remove(curr_edge.v1)
            except:
                pass
    
    print(new_graph)
    visited = []
    dfs(new_graph, edge.v1, visited)
    print(visited)
    return edge.v2 in visited

    

if __name__ == "__main__":
    graph = {
  5 : [3,7],
  3 : [2, 4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}
m = 0
for i in graph:
    m += len(graph[i])

print(m)


lst_edges = []
for i in graph:
    for j in graph[i]:
        lst_edges.append(Edge(i, j, i))

for elm in lst_edges:
    print(elm)

visited = []
print(dfs(graph, 5, visited))
print(visited)
print(solve(Edge(5, 3, 3), graph, lst_edges))
