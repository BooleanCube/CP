n,m=map(int,input().split())
l=list(map(int,input().split()))
c = 0
ans = []
for i in range(n):
    c += l[i]
    ans.append(c//m)
    c %= m
print(*ans)