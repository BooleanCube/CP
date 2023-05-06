t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = 0
    c = 1 if l[0] == 0 else 0
    for i in range(1, n):
        if l[i] == 0:
            c += 1
        else:
            m = max(m, c)
            c = 0
    m = max(m, c)
    print(m)
