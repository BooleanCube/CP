t = int(input())
for l in range(t):
    n, c = map(int, input().split())
    p = list(map(int, input().split()))
    m = {}
    for i in range(1, n+1):
        e = p[i-1]
        if e not in m:
            m[e] = []
        m[e].append(i)
    s = 0
    for i in m:
        if len(m[i]) > c: s+=c
        else: s+=len(m[i])
    print(s)
