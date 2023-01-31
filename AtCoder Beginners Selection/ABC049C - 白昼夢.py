S = input()
rS = S[::-1]
parts = ["dream", "dreamer", "erase", "eraser"]
checked = True
while checked:
    checked = False
    for part in parts:
        if rS.find(part[::-1]) == 0:
            checked = True
            rS = rS[len(part) :]
            break

if len(rS) == 0:
    print("YES")
else:
    print("NO")
