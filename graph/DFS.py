from graph import Graph, Vertex


def DFS(G):

    def DFS_visit(G, vertex):
        nonlocal time
        time += 1
        vertex.distance = time
        vertex.color = 1
        for i in vertex:
            if G[i].color == 0:
                G[i].parent = vertex
                DFS_visit(G, G[i])
        vertex.color = 2
        time += 1
        vertex.distance = time

    for vertex in G:
        G[vertex].color = 0
        G[vertex].parent = None
    time = 0
    for vertex in G:
        if G[vertex].color == 0:
            DFS_visit(G, G[vertex])


if __name__ == '__main__':
    G = Graph()
    G.insert(Vertex('s'), Vertex('r'), Vertex('v'), Vertex('w'), Vertex('x'),
        Vertex('t'), Vertex('u'), Vertex('y'))
    G['s'].add_edge('r', 'w')
    G['r'].add_edge('v')
    G['w'].add_edge('t', 'x')
    G['t'].add_edge('u', 'x')
    G['x'].add_edge('t', 'u', 'y')
    G['u'].add_edge('t', 'x', 'y')
    G['y'].add_edge('x', 'u')
    DFS(G)
    for i in G:
        print(f"{i}: {G[i].distance}")
    # print_path(G, G['s'], G['y'])
