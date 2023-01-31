N, L = list(map(int, input().split()))
K = int(input())
AN = list(map(int, input().split()))

dn = []
for i, a in enumerate(AN):
    if i == 0:
        dn.append(a)
    else:
        dn.append(a - AN[i - 1])
dn.append(L - AN[-1:][0])
# print(dn)


def canCut(m):
    cut_count = K
    sum_count = 0
    for i, d in enumerate(dn):
        sum_count += d
        if sum_count >= m:
            if cut_count != 0:
                cut_count -= 1
                sum_count = 0

    if sum_count >= m:
        # print(cut_count, sum_count, True)
        return True
    else:
        # print(cut_count, sum_count, False)
        return False


found = False
left, right = 1, L - 1

while not found:
    middle = int((right - left) / 2)
    # print(left, middle, right)
    if canCut(left + middle):
        left += middle
    else:
        right -= middle
    if middle == 0:
        found = True
print(left)
