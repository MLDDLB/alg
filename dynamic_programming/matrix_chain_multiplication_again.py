import time

# O(n) memmory (recursion) and Omega(2^n) time
def recursive_matrix_chain(p, i, j):
    if i == j:
        return 0
    m = float('inf')
    for k in range(i, j):
        q = (recursive_matrix_chain(p, i, k)
                + recursive_matrix_chain(p, k+1, j) + p[i-1]*p[k]*p[j])
        if q < m:
            m = q
    return m

# O(n^2) memmory and O(n^3) time
def bottom_up_matrix_chain(p):
    n = len(p)
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for i in range(n)]
    for l in range(2, n):
        for i in range(1, n-l+1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return (m, s)

# O(n^2) memmory + recursion and O(n^3) time
def memoized_matrix_chain(p):
    n = len(p)
    m = [[float('inf') for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        m[i][i] = 0
    return lookup_matrix_chain(p, m, s, 1, n-1)

def lookup_matrix_chain(p, m, s, i, j):
    if m[i][j] < float('inf'):
        return (m[i][j], s)
    else:
        for k in range(i, j):
            q = (lookup_matrix_chain(p, m, s, i, k)[0]
                    + lookup_matrix_chain(p, m, s, k+1, j)[0] + p[i-1]*p[k]*p[j])
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = k
        return (m[i][j], s)

# Construct a solution
def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end = '')
    else:
        print('(', end = '')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(')', end = '')

p = [30, 35, 15, 5, 10, 20, 25]
clock = time.time()
print(f"(simple recursive algorithm) minimal amount of multiplications: {recursive_matrix_chain(p, 1, 6)}\ntime = {time.time() - clock}")
clock = time.time()
print(f"(bottom-up algorithm) minimal amount of multiplications: {bottom_up_matrix_chain(p)[0][1][6]}\ntime = {time.time() - clock}")
clock = time.time()
print(f"(bottom-up algorithm) minimal amount of multiplications: {memoized_matrix_chain(p)[0]}\ntime = {time.time() - clock}")
m, s = bottom_up_matrix_chain(p)
print_optimal_parens(s, 1, 6)
s = memoized_matrix_chain(p)[1]
print_optimal_parens(s, 1, 6)
