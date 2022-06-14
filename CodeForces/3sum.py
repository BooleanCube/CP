t=int(input())
for i in range(t):
    input()
    a=list(map(int,input().split()))
    b=[j%10 for j in a]
    c=list(set(b))
    no= True
    for j in range(len(c)):
        for k in range(j+1,len(c)):
            for l in range(k+1,len(c)):
                if (c[j]+c[k]+c[l])%10==3:
                    if no:print("YES")
                    no=False
                    break
    if no: print("NO")
