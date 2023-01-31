N, A, B = list(map(int, input().split(" ")))
asum = 0
for n in range(N + 1):
    s = sum([int(nn) for nn in str(n)])
    if s >= A and s <= B:
        asum += n
print(asum)
