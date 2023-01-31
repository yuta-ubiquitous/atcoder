# N, L = list(map(int, input().split()))
# K = int(input())
# AN = list(map(int, input().split()))

N, L = 3, 34
K = 1
AN = [8, 13, 26]

dn = []
for i, a in enumerate(AN):

    if i == 0:
        dn.append(a)
    else:
        dn.append(a - AN[i - 1])
dn.append(L - AN[-1:][0])


def canCut(m):
    print(m)
    print(dn)
    cut_count=0
    for i, d in enumerate(dn):
        left = 


canCut(1)
