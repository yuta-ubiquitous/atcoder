A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
for an in range(A + 1):
    for bn in range(B + 1):
        for cn in range(C + 1):
            if an * 500 + bn * 100 + cn * 50 == X:
                count += 1
print(count)
