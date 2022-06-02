def LCS_length(x,y):
    m = len(x)
    n = len(y)
    b = [[0 for i in range(m+1)] for j in range(n+1)]
    c = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(0,m):
        for j in range(0,n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 2
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 3
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 1
    return (c, b)

def print_lcs(b, x, i, j):
    if i == -1 or j == -1:
        return
    print(f"i = {i}, j = {j}")
    if b[i][j] == 2:
        print_lcs(b, x, i-1, j-1)
        print(x[i])
    elif b[i][j] == 3:
        print_lcs(b, x, i-1, j)
    else:
        print_lcs(b, x, i, j-1)

x = ['a', 'b', 'c', 'b', 'd', 'a', 'b']
y = ['b', 'd', 'c', 'a', 'b', 'a']
print_lcs(LCS_length(x, y)[1], x, len(x)-1, len(y)-1)
