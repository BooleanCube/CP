t = int(input())
for z in range(t):
    n,q = map(int,input().split())
    l = list(map(int, input().split()))
    co = len([1 for i in l if i%2])
    ce = n-co
    s = sum(l)
    for y in range(q):
        o,v = map(int, input().split())
        if o:
            s+=co*v
            if v%2: co = 0;ce = n
        else:
            s+=ce*v
            if v%2: ce = 0;co = n
        print(s)

