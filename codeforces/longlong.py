t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l = [i for i in l if i!=0]
    n = len(l)
    if n < 1:
        print(0,0)
        continue
    p = l[0]
    ans = 0
    for i in range(1, n):
        if p<0 and l[i]>0:
            ans += 1
        p = l[i]
    if p<0: ans += 1
    print(sum(abs(c) for c in l), ans)
