import time

def cut_rod_recursive(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        print(f"before: q = {q}, p[{i}] = {p[i]}")
        q = max(q, p[i] + cut_rod_recursive(p, n-i))
        print(f"after: q = {q}, p[{i}] = {p[i]}")
    return q

def memoized_cut_rod(p, n):
    r = [float('-inf') for i in range(n+1)]
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        print(f"r = {r}, r[{n}] = {r[n]}")
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    print(f"r = {r}, r[{n}] = {r[n]}")
    return q

def bottom_up_cut_rod(p, n):
    r = [float('-inf') for i in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
        print(f"r = {r}, r[{j}] = {r[j]}")
    return r[n]

def extended_bottom_up_cut_rod(p, n):
    r = [float('-inf') for i in range(n+1)]
    s = [0 for i in range(n+1)]
    r[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
        print(f"r = {r}, r[{j}] = {r[j]}, s = {s}, s[{j}] = {s[j]}")
    return (r, s)

def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        time.sleep(1)
        print(s[n])
        n = n - s[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print("Optimal cut = {}".format(cut_rod_recursive(p, 4)))
print("Optimal cut = {}".format(memoized_cut_rod(p, 4)))
print("Optimal cut = {}".format(bottom_up_cut_rod(p, 4)))
print_cut_rod_solution(p, 4)
