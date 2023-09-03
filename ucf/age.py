o, a, k = map(int, input().split())
c,d = a, k
ans = 0
while c<o:
    if (o-c)%k == 0:
        ans = 1
    c += a
print(ans)
