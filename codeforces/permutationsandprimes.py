p = [1]*(300001)
p[0] = p[1] = 0
for i in range(2, len(p)):
    for j in range(i*2, len(p), i):
        p[j] = 0

tc = int(input())
for _ in range(tc):
    n = int(input())
    ps = [i for i in range(1,n+1) if p[i]][::-1]
    nps = [i for i in range(2, n+1) if not p[i]]
    s = ps[0:len(ps):2]
    e = ps[1:len(ps):2]
    print(*(s + nps[:len(nps)//2] + [1] + nps[len(nps)//2:] + e))
