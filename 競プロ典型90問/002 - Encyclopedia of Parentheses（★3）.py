N = int(input())
bit_list = [str(bin(i))[2:] for i in range(2**N)]
max_len = max(map(len, bit_list))

for i in bit_list:
    kn = i.zfill(max_len)

    l_count = 0
    r_count = 0
    check = True
    for i, k in enumerate(kn):
        if k == "0":
            l_count += 1
        else:
            r_count += 1
        if l_count < r_count:
            check = False
            break

    if l_count == r_count and check:
        print(kn.replace("0", "(").replace("1", ")"))
