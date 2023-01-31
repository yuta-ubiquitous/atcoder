parts = ["dream", "dreamer", "erase", "eraser", "e", "r", "e", "r", "e", "r"]
import random

random.seed(0)

for _ in range(200):
    f = open(f"abc049c/abc049c_testcase_{_}.txt", mode="w")
    surplus = random.randint(1, 1000 / 5)
    T = ""
    while surplus > 0:
        picked = parts[random.randint(0, len(parts) - 1)]
        T += picked
        surplus -= len(picked)
    f.write(T)
    f.close()
