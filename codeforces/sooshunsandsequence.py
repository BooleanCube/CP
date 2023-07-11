n, k = map(int, input().split())
l = list(map(int, input().split()))
if len(set(l[k-1:])) > 1:
    print(-1)
    exit(0)
exp = l[k-1]
ans = 0
for i in range(n-1, -1, -1):
    if l[i] != exp:
        ans = i+1
        break
print(ans)
