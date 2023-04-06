t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    f = 1
    for x in range(256):
        a = [i^x for i in l]
        total = a[0]
        for i in range(1, n):
            total ^= a[i]
        if total == 0:
            print(x)
            f = 0
            break
    if f:
        print(-1)
