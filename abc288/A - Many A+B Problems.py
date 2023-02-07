N = int(input())
abn = []
for _ in range(N):
    abn.append(list(map(int, input().split())))
for ab in abn:
    print(sum(ab))
