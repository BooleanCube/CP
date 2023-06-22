t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    while n > 0:
        s += n
        n >>= 1
    print(s)
