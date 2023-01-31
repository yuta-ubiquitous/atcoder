N = int(input())
AN = list(map(int, input().split(" ")))

counter = 0
while all(list(map(lambda a: a % 2 == 0, AN))):
    AN = list(map(lambda a: int(a / 2), AN))
    counter += 1

print(counter)
