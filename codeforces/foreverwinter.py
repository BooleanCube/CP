t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    f = {}
    ff = {}
    for i in range(m):
        u,v = map(int, input().split())
        if u in f:
            f[u] += 1
        else: f[u] = 1
        if v in f:
            f[v] += 1
        else: f[v] = 1
    for i in f:
        if f[i] in ff:
            ff[f[i]] += 1
        else: ff[f[i]] = 1
    l = sorted([(ff[k],k) for k in ff])
    b = l[1][1]
    if l[1][0] == l[2][0]:
        b = max(l[1][1], l[2][1])
    print(l[0][1], b-1)
