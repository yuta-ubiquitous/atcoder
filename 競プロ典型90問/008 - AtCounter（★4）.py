n = int(input())
si = input()

si += "-"
atcoder = "atcoder+"


dp = [[] for _ in range(len(si))]
for i in range(len(dp)):
    dp[i].extend([0 for _ in range(len(atcoder))])

dp[0][0] = 1

for i in range(len(dp)):
    if i == len(si) - 1:
        continue
    for j in range(len(dp[i])):
        if j == len(atcoder):
            continue

        if si[i] == atcoder[j]:
            dp[i + 1][j + 1] += dp[i][j]
        dp[i + 1][j] += dp[i][j]


print(dp[len(si) - 1][len(atcoder) - 1] % (10 ** 9 + 7))
