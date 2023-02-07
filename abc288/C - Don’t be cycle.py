from typing import Dict, List
import sys

sys.setrecursionlimit(10 ** 6)
n, m = list(map(int, input().split()))

abm = []
for _ in range(m):
    abm.append(list(map(int, input().split())))

graph: Dict[int, List[int]] = dict(zip(range(1, n + 1), [[] for _ in range(n)]))

for u, v in abm:
    graph[u].append(v)
    graph[v].append(u)

seen = {}
for v in range(1, n + 1):
    seen[v] = False


def dfs(graph, v):
    global seen
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v)


s = 0
for v, is_seen in seen.items():
    if not is_seen:
        s += 1
        dfs(graph, v)
print(m - n + s)
