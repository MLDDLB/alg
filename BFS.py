import sys
from collections import deque
import time

def BFS(arr, u, v):
    distances = [-1 for i in range(len(arr))]
    distances[u] = 0
    versh_queue = deque()
    versh_queue.append(u)
    while versh_queue:
        node = versh_queue.popleft()
        for i in arr[node]:
            #if i == v:
                #distances[i-1] = distances[node-1] + 1
                #return distances[v-1]
            if distances[i] < 0:
                if i == v:
                    distances[i] = distances[node] + 1
                    return distances[v]
                versh_queue.append(i)
                distances[i] = distances[node] + 1
    return distances[v]


city_count = int(sys.stdin.readline().strip())

#clock = time.time_ns()
coord_list = []
for i in range(city_count):
    coord_list.append(sys.stdin.readline().strip().split())
#print("coord_list time = {}".format(time.time_ns() - clock))

poss_dist = int(sys.stdin.readline().strip())

fr_to = sys.stdin.readline().strip().split()
from_index = int(fr_to[0])
to_index = int(fr_to[1])

#clock = time.time_ns()
city_dict = [[] for i in range(city_count)]
#print("city_dict time = {}".format(time.time_ns() - clock))

clock = time.time()
for i in range(city_count):
    for j in range(i, city_count):
        if (abs(int(coord_list[j][1]) - int(coord_list[i][1])) + abs(int(coord_list[j][0]) - int(coord_list[i][0]))) <= poss_dist:
            city_dict[i].append(j)
            city_dict[j].append(i)
#print("graph time = {}".format(time.time_ns() - clock))

#clock = time.time_ns()
dist = BFS(city_dict, from_index - 1, to_index - 1)
#print("BFS time = {}".format(time.time_ns() - clock))
print(dist)
print("clock = {}".format(time.time() - clock))
