import sys

sys.setrecursionlimit(10 ** 6)

H, W = list(map(int, input().split()))
Q = int(input())

matrix = []
for _ in range(H):
    matrix.append([False for _ in range(W)])

trees = []
for i in range(H):
    for j in range(W):
        trees.append(-1)


def root(pos):
    np = trees[pos]
    if np == -1:
        return pos
    trees[pos] = root(trees[pos])
    return trees[pos]


def union(ra, ca, rb, cb):
    apos = root(ra * W + ca)
    bpos = root(rb * W + cb)
    if apos == bpos:
        return
    trees[apos] = bpos


for _ in range(Q):
    q = list(map(int, input().split()))
    t = q[0]
    if t == 1:
        r, c = q[1:]
        r -= 1
        c -= 1
        matrix[r][c] = True

        for x, y in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            if r + x < 0 or c + y < 0 or r + x == H or c + y == W:
                continue
            if matrix[r][c] and matrix[r + x][c + y]:
                union(r, c, r + x, c + y)
    else:
        ra, ca, rb, cb = q[1:]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        if root(ra * W + ca) == root(rb * W + cb) and matrix[ra][ca] and matrix[rb][cb]:
            print("Yes")
        else:
            print("No")
