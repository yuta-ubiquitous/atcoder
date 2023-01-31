n = int(input())
s = input()
for i, s in enumerate(s):
    if s == "1":
        if i % 2 == 0:
            print("Takahashi")
            break
        else:
            print("Aoki")
            break
