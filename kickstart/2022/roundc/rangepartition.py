t=int(input())
for i in range(t):
    n,x,y=map(int, input().split())
    r=x/y
    l=[1]
    a=1
    b=n*(n+1)//2-1
    d=False
    for j in range(n):
        if a/b==r:
            print("Case #"+str(i+1)+": POSSIBLE")
            print(len(l))
            print(" ".join(map(str,l)))
            d=True
            break
        c=a+1
        a+=c
        b-=c
        l.append(c)
    if not d: print("Case #"+str(i+1)+": IMPOSSIBLE")
