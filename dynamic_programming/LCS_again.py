import time

# O(mn) memmory O(mn) time
def bottom_up_lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[float('inf') for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        c[i][0] = 0
    for j in range(0, n+1):
        c[0][j] = 0
    for i in range(0, m):
        for j in range(0, n):
            if x[i] == y[j]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                if c[i][j+1] >= c[i+1][j]:
                    c[i+1][j+1] = c[i][j+1]
                else:
                    c[i+1][j+1] = c[i+1][j]
    return c

# O(mn) memmory and O(mn) time
def memoized_lcs_length(x,y):
    m = len(x)
    n = len(y)
    c = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        c[i][0] = 0
    for j in range(0, n+1):
        c[0][j] = 0
    return memoized_lcs_length_aux(c, x, y, m, n)

def memoized_lcs_length_aux(c, x, y, i, j):
    if c[i][j] >= 0:
        return c
    else:
        if x[i-1] == y[j-1]:
            c[i][j] = memoized_lcs_length_aux(c, x, y, i-1, j-1)[i-1][j-1] + 1
        else:
            c[i-1][j] = memoized_lcs_length_aux(c, x, y, i-1, j)[i-1][j]
            c[i][j-1] = memoized_lcs_length_aux(c, x, y, i, j-1)[i][j-1]
            if c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
        return c

def print_lcs(c, x, y, i, j):
    if i == 0 or j == 0:
        return 0
    if x[i-1] == y[j-1]:
        print_lcs(c, x, y, i-1, j-1)
        print(x[i-1], end = '')
    else:
        if c[i-1][j] >= c[i][j-1]:
            print_lcs(c, x, y, i-1, j)
        else:
            print_lcs(c, x, y, i, j-1)


x = 'ABCDBAB'
y = 'BDCABA'
clock = time.time()
c1 = bottom_up_lcs_length(x, y)
print(f"(bottom-up algorithm) LCS length = {c1[len(x)][len(y)]}\ntime = {time.time()-clock}")
c2 = memoized_lcs_length(x, y)
print(f"(memoized algorithm) LCS length = {c2[len(x)][len(y)]}\ntime = {time.time()-clock}")
print_lcs(c1, x, y, len(x), len(y))
print()
print_lcs(c2, x, y, len(x), len(y))
