n, x = map(int, input().split(" "))
ai = list(map(int, input().split(" ")))

for index, a in enumerate(ai):
    if (index + 1) % 2 == 0:
        x -= a - 1
    else:
        x -= a

if x >= 0:
    print("Yes")
else:
    print("No")
