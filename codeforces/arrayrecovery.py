t=int(input())
for z in range(t):
    n=int(input())
    l = list(map(int,input().split()))
    r = []
    flag = True
    for i in range(n):
        if i==0: r.append(l[i])
        else:
            if l[i]==0: r.append(r[i-1])
            elif l[i]>r[i-1]:r.append(r[i-1]+l[i])
            else: flag=False;break
    if flag:print(*r)
    else:print(-1)
