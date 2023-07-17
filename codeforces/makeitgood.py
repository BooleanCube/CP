tc = int(input())
for _ in range(tc):
    n = int(input())
    l = list(map(int, input().split()))
    if n<2:
        print(0)
        continue
    e = 1
    ans = 0
    p = l[-1]
    for i in range(n-2, -1, -1):
        if e>0 and l[i]<p:
            e=0
        elif e<1 and l[i]>p:
            ans=i+1
            break
        p = l[i]
    print(ans)
