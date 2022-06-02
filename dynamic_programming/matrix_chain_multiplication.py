import time

def matrix_chain_order(p):
    n = len(p)
    m = [[0 for i in range(0,n)] for j in range(n)]
    s = [[0 for k in range(n)] for l in range(n)]
    for l in range(2, n+1):
        for i in range(0, n-l):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j]+p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    print(m[0][5])
    time.sleep(2)
    return (m,s)

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}")
    else:
        print("(")
        print_optimal_parens(s,i,s[i][j])
        print_optimal_parens(s,s[i][j]+1,j)
        print(")")

def recursive_matrix_chain(p, i, j):
    if i == j:
        return 0
    m = float('inf')
    for k in range(i, j):
        q = (recursive_matrix_chain(p, i, k) + recursive_matrix_chain(p, k+1, j)
                + p[i]*p[k+1]*p[j+1])
        if q < m:
            m = q
    return m

def memoized_matrix_chain(p):
    n = len(p)-1
    m = [[float('inf') for i in range(n)] for j in range(n)]
    print(m)
    return lookup_chain(m, p, 0, n-1)

def lookup_chain(m, p, i, j):
    if m[i][j] < float('inf'):
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = (lookup_chain(m, p, i, k)
                    + lookup_chain(m, p, k+1, j) + p[i]*p[k+1]*p[j+1])
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]

p = [5, 10, 3, 12, 5, 50, 5]
print_optimal_parens(matrix_chain_order(p)[1], 0, 5)
print(recursive_matrix_chain(p, 0, 5))
print(memoized_matrix_chain(p))
