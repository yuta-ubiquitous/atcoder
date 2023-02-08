n = int(input())
an = list(map(int, input().split()))
q = int(input())
bq = [int(input()) for _ in range(q)]

import bisect

sorted_an = sorted(an)

for b in bq:
    index = bisect.bisect(sorted_an, b)
    if index == 0:
        print(abs(b - sorted_an[index]))
    elif index == n:
        print(abs(b - sorted_an[index - 1]))
    else:
        left_score = abs(b - sorted_an[index - 1])
        right_score = abs(b - sorted_an[index])
        if left_score < right_score:
            print(left_score)
        else:
            print(right_score)
