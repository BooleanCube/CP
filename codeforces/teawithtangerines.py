t=int(input())
for z in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    p=l[0]
    d = p*2
    s=0
    for i in l[1:]:
        v = (i+d-2)//(d-1)-1
        s+=v
    print(s)
