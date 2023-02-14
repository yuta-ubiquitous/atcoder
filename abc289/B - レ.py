N, M = list(map(int, input().split()))
am = list(map(int, input().split()))
# N, M = 5, 3
# am = [1, 3, 4]

graph = []
g = []
for i in range(0, N):
    if i + 1 in am:
        g.append(i + 1)
    else:
        g.append(i + 1)
        graph.append(g)
        g = []

first = True
for ps in graph:
    for p in ps[::-1]:
        if first:
            print(p, end="")
            first = False
        else:
            print(f" {p}", end="")
print()
