from math import log2 as lg

n = int(input())

for _ in range(n):
    a, b, r = map(int, input().split())
    if a > b: a, b = b, a
    x, f = 0, 1
    for bit in range(63, -1, -1):
        abit = a & (1 << bit)
        bbit = b & (1 << bit)
        if abit != bbit and f: f = 0
        elif abit != bbit and bbit and (x ^ (1 << bit)) <= r:
            x ^= (1 << bit)
    # print(x, a^x, b^x)
    print(abs((a ^ x) - (b ^ x)))