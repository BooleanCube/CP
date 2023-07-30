import math

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    c = sum(1 for i in range(1, n+1) if l[i-1]==i)
    print(0 if c==0 else math.ceil(c/2))
