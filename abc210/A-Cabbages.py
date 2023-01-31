n, a, x, y = map(int, input().split(" "))

if a > n:
    print(n * x)
else:
    print(a * x + (n - a) * y)
