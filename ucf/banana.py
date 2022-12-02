import math
import itertools

def dist(a,b):
    return math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2))

def mindist(a,b):
    s = 0
    for i in a:
        m = 1e10
        idx = -1
        for k in range(len(b)):
            j = b[k]
            d = dist(i,j)
            if d<m:
                m=d
                idx=k
        s += m
        b.pop(idx)
    return s


t = int(input())
for z in range(t):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    b = [list(map(int,input().split())) for _ in range(n)]
    o = b.copy()
    l = itertools.permutations(a)
    m = 1e10
    for i in l:
        m = min(m, mindist(i,b))
        b = o.copy()
    print(m)
