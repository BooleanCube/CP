import math

t = int(input())
for z in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if math.gcd(*l) == 1: print(0);continue
    o = l[-1]
    l[-1] = math.gcd(l[-1],n)
    if math.gcd(*l) == 1: print(1);continue
    l[-1] = o
    l[-2]= math.gcd(l[-2],n-1)
    if math.gcd(*l) == 1: print(2);continue
    else: print(3)
