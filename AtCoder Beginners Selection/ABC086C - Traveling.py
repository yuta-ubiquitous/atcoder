N = int(input())
txyn = []
for _ in range(N):
    txyn.append(list(map(int, input().split())))

cannot = False
pt, px, py = 0, 0, 0
for txy in txyn:
    t, x, y = txy
    dt = t - pt
    dist = abs(x - px) + abs(y - py)
    if dt < dist:
        cannot = True
    if dt % 2 != dist % 2:
        cannot = True
    pt, px, py = t, x, y

if cannot:
    print("No")
else:
    print("Yes")

import os
os.pathsep
