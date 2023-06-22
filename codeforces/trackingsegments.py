t = int(input())
l = []
for _ in range(t):
    n,m = map(int, input().split())
    c = {}
    for i in range(m):
        a,b = map(int, input().split())
        c[(a,b)] = 0
    q = int(input())
    ans = -1
    for i in range(q):
        u = int(input())
        if ans > -1: continue
        for k in c:
            a,b = k
            if a<=u<=b:
                c[k] += 1
            if c[k] > (b-a+1)/2:
                ans = i+1
    l.append(ans)
print("\n".join(map(str, l)))
