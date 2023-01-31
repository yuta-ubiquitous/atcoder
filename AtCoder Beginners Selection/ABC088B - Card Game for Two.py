N = int(input())
an = list(map(int, input().split(" ")))
an.sort(reverse=True)
alice, bob = 0, 0
alice = sum([a for i, a in enumerate(an) if i % 2 == 0])
bob = sum([a for i, a in enumerate(an) if i % 2 == 1])
print(alice - bob)
