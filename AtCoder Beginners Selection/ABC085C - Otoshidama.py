N, Y = list(map(int, input().split()))
pair = None
for i in range(N + 1):
    if pair:
        break
    for g in range(N - i + 1):
        s = N - i - g
        if s < 0:
            continue
        otoshidama = i * 10000 + g * 5000 + s * 1000
        if otoshidama == Y:
            pair = [i, g, s]
            break
if pair is None:
    pair = [-1, -1, -1]
print(f"{pair[0]} {pair[1]} {pair[2]}")
