t = int(input())
for z in range(t):
    n = int(input())
    s = 2050000000000000000
    count = 0
    for i in range(16):
        c = n // s
        count += c
        n -= s * c
        s //= 10
    print(-1 if n > 0 else count)
