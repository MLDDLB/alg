# Given a set S = {a1, a2, ..., an}, that consists of n activities.
# Each acitivity has a starting time and an ending time si and fi
# Find the largest set of compatible activities

#O(n) time and O(n) memmory (recursive calls and a set)
def recursive_activity_selector(s, f, k, n):
    m = k+1
    while m < n and s[m] < f[k]:
        m += 1
    if m < n:
        return {m}.union(recursive_activity_selector(s, f, m, n))
    else:
        return set()

#O(n) time and O(n) memmory (set) but no recursion which is good
def greedy_activity_selector(s, f, n):
    max_set = {1}
    k = 1
    for m in range(n):
        if s[m] >= f[k]:
            max_set.add(m)
            k = m
    return max_set


def dynamic_activity_selector(s, f):
    n = len(s)
    s.append(f[n-1])
    c = [[0 for i in range(n+1)] for j in range(n+1)]
    d = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(0, n):
        c[i][i] = 0
        c[i][i+1] = 0
    c[i+1][i+1] = 0
    for l in range(2, n+2):
        print(f"l = {l}")
        for i in range(0, n-l+1):
            j = i+l
            print(f"j = {j}")
            k = i
            while k < j:
                if f[i] <= s[k] and f[k] <= s[j]:
                    q = c[i][k] + c[k][j] + 1
                    print(f"q = {q}; i = {i}; j = {j}; k = {k}")
                    if c[i][j] < q:
                        c[i][j] = q
                        d[i][j] = k
                k += 1
    s.pop()
    return (c, d)

def print_max_set(d, i, j):
    if d[i][j] == 0:
        return
    else:
        print(d[i][j], end = " ")
        print_max_set(d, i, d[i][j])
        print_max_set(d, d[i][j], j)


s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
max_set = recursive_activity_selector(s, f, 0, len(s))
print(max_set)
print(greedy_activity_selector(s, f, len(s)))
c, d = dynamic_activity_selector(s, f)
print(c)
print(c[0][len(f)])
print(d)
print_max_set(d, 0, len(s))
