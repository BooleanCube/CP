t=int(input())
for z in range(t):
    n,x,y=map(int,input().split())
    if x==y==0: print(-1)
    elif x>0 and y>0: print(-1)
    else:
        ans = []
        x = max(x,y)
        if (n-1)%x == 0:
            c = (n-1)//x
            a = 1
            for y in range(c):
                ans += [a]*x
                if a==1: a+=1
                a += x
        else: print(-1);continue
        print(*ans)
