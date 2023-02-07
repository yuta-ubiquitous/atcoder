n, k = list(map(int, input().split()))
sn = []
for _ in range(n):
    sn.append(input())

joui = sorted(sn[:k])
for s in joui:
    print(s)
