import math
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=True
    for j in set(l):
        if l.count(j)>math.ceil(n/2): a=False
    print("YES" if a else "NO")
#thats kinda funny
