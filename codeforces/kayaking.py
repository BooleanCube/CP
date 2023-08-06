n = int(input())
l = sorted(map(int, input().split()))

ans = 1e9
for i in range(len(l)):
    for j in range(i+1, len(l)):
        a = [l[x] for x in range(len(l)) if not (x==i or x==j)]
        cur = 0
        for idx in range(len(a)//2):
            cur += a[idx*2+1]-a[idx*2]
        ans = min(ans, cur)
print(ans)
