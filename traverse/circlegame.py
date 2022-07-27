t=int(input())
for i in range(t):
    n=int(input())
    if n%2==0:
        input()
        print("Mike")
    else:
        l=list(map(int,input().split()))
        m=min(l)
        j=l.index(m)
        if j%2==0 and l.count(m) == 1:print("Mike")
        else: print("Joe")
