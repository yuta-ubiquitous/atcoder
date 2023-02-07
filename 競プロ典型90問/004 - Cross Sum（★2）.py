h, w = list(map(int, input().split()))
ahw = []
for aw in range(h):
    ahw.append(list(map(int, input().split())))

sh = []
sw = []
for i in range(h):
    sh.append(sum(ahw[i]))

for i in range(w):
    s = 0
    for j in range(h):
        s += ahw[j][i]
    sw.append(s)

for i in range(h):
    for j in range(w):
        result = sh[i] + sw[j] - ahw[i][j]
        if j == (w - 1):
            print(result, end="")
        else:
            print(result, end=" ")
    print()
