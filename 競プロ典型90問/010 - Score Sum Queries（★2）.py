N = int(input())
CPi = []
CumulativeCPi = [[0], [0]]
for i in range(N):
    cp = list(map(int, input().split()))
    if cp[0] == 1:
        CumulativeCPi[0].append(CumulativeCPi[0][i] + cp[1])
        CumulativeCPi[1].append(CumulativeCPi[1][i])
    else:
        CumulativeCPi[0].append(CumulativeCPi[0][i])
        CumulativeCPi[1].append(CumulativeCPi[1][i] + cp[1])
    CPi.append(cp)
Q = int(input())
LRQ = []
for _ in range(Q):
    LRQ.append(list(map(int, input().split())))

for l, r in LRQ:
    print(
        CumulativeCPi[0][r] - CumulativeCPi[0][l - 1],
        CumulativeCPi[1][r] - CumulativeCPi[1][l - 1],
    )
