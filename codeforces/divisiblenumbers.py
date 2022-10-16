from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

t = int(input())
for z in range(t):
    a,b,c,d = map(int, input().split())
    o = a*b
    m = o
    n = c*d
    f = True
    while m<n:
        m += o
        #print(m)
        f = list(factors(m))
        #print(f)
        l = [i for i in f if a<i<=c and b<m//i<=d]
        #print(l)
        if len(l) > 0: print(l[0], m//l[0]);f=False;break
    if f:print(-1,-1)
