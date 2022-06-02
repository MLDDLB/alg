from graph import Graph, Vertex

def BFS(G, s):
    for i in G:
        G[i].color = 0
        G[i].parent = None
        G[i].distance = float('inf')
    s.color = 1
    s.distance = 0
    s.parent = None
    q = []
    q.append(s)
    while q:
        cur_vert = q.pop(0)
        for edge in cur_vert:
            if G[edge].color == 0:
                G[edge].color = 1
                G[edge].parent = cur_vert
                G[edge].distance = cur_vert.distance+1
                q.append(G[edge])
        cur_vert.color = 2

def print_path(G, s, v):
    if v.key == s.key:
        print(s.key)
    elif v.parent is None:
        print('No path')
    else:
        print_path(G, s, v.parent)
        print(v.key)


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
    BFS(G, G['s'])
    for i in G:
        print(f"{i}: {G[i].distance}")
    print_path(G, G['s'], G['y'])
