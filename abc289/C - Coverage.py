N, M = list(map(int, input().split()))
SM = []
for _ in range(M):
    input()
    SM.append(list(map(int, input().split())))

ans = 0
for b in range(2 ** M):
    s = set()
    for i in range(M):
        if (b >> i) & 1:
            s |= set(SM[i])
    if len(s) == N:
        ans += 1

print(ans)
