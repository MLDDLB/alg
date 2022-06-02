import time

# O(2^n) time
def cut_rod_recursive(p, n):
    if n == 0:
        return p[0]
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod_recursive(p, n-i))
    return q

# O(n^2) time and O(n) memmory
def memoized_cut_rod(p, n):
    r = [float('-inf') for i in range(n+1)]
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q

# O(n^2) time and O(n) memmory, but no recursion
def bottom_up_cut_rod(p, n):
    r = [float('-inf') for i in range(n+1)]
    r[0] = 0
    for i in range(1, n+1):
        q = float('-inf')
        for j in range(1, i+1):
            q = max(q, p[j] + r[i-j])
        r[j] = q
    return r[n]

# O(n^2) time and O(n) memmory and it memmorizes the solution
def extended_bottom_up_cut_rod(p, n):
    r = [float('-inf') for i in range(n+1)]
    s = [float('-inf') for i in range(n+1)]
    r[0], s[0] = (0, 0)
    for i in range(1, n+1):
        q = float('-inf')
        for j in range(1, i+1):
            if q < p[j] + r[i-j]:
                q = p[j] + r[i-j]
                s[i] = j
        r[i] = q
    return (r, s)

def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n], end = ' ')
        n -= s[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
clock = time.time()
print(f'(simple recursive algorithm) highest revenue for n = 9: {cut_rod_recursive(p, 9)}\ntime = {time.time()-clock}')
clock = time.time()
print(f"(top-down algorithm) highest revenue for n = 9: {memoized_cut_rod(p, 9)}\ntime = {time.time()-clock}")
clock = time.time()
print(f"(bottom-up algorithm) highest revenue for n = 9: {bottom_up_cut_rod(p, 9)}\ntime = {time.time()-clock}")
clock = time.time()
print(f"(bottom-up algorithm) highest revenue for n = 9: {extended_bottom_up_cut_rod(p, 9)[0][9]}\ntime = {time.time()-clock}")
print("Solution: ")
print_cut_rod_solution(p, 9)
