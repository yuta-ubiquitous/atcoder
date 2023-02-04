from typing import Dict, List
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
abn = []
for _ in range(n - 1):
    abn.append(list(map(int, input().split())))

graph: Dict[int, List[int]] = dict(zip(range(1, n + 1), [[] for _ in range(n)]))

for u, v in abn:
    graph[u].append(v)
    graph[v].append(u)

seen = {}
for v in range(1, n + 1):
    seen[v] = False

max_depth = 0
max_depth_v = 0


def search(graph, v, depth=0):

    global max_depth
    global max_depth_v

    if max_depth < depth:
        max_depth = depth
        max_depth_v = v

    global seen
    seen[v] = True

    for next_v in graph[v]:

        if seen[next_v]:
            continue
        search(graph, next_v, depth + 1)


search(graph, 1)
seen = {}
for v in range(1, n + 1):
    seen[v] = False
max_depth = 0
search(graph, max_depth_v)

print(max_depth + 1)
