from graph import Graph, Vertex
from collections import deque

def DFS_topological(G, sorted_list):

    def DFS_visit(G, vertex):
        nonlocal time
        time += 1
        vertex.distance = time
        vertex.color = 1
        for edge in vertex:
            if G[edge].color == 0:
                G[edge].parent = vertex
                DFS_visit(G, G[edge])
        vertex.color = 2
        time += 1
        vertex.distance = time
        sorted_list.appendsleft(vertex)

    for vertex in G:
        G[vertex].color = 0
        G[vertex].parent = None
    time = 0
    for vertex in G:
        if G[vertex].color == 0:
            DFS_visit(G, G[vertex])


def topological_sort(G):
    sorted_list = deque()
    DFS_topological(G, sorted_list)
    return sorted_list


if __name__ == '__main__':
    G = Graph()
    G.insert(Vertex('Рубашка'), Vertex('Ремень'), Vertex('Галстук'), Vertex('Пиджак'),
        Vertex('Брюки'), Vertex('Трусы'), Vertex('Туфли'), Vertex('Носки'), Vertex('Часы'))
    G['Трусы'].add_edge('Брюки', 'Туфли')
    G['Брюки'].add_edge('Туфли', 'Ремень')
    G['Ремень'].add_edge('Пиджак')
    G['Рубашка'].add_edge('Ремень', 'Галстук')
    G['Галстук'].add_edge('Пиджак')
    G['Носки'].add_edge('Туфли')
    sorted_vertex_list = topological_sort(G)
    print(sorted_vertex_list)
