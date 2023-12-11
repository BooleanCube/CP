n, k = map(int, input().split())

par = [i for i in range(n)]

def find(x):
    if (x%n) == par[x]: return x
    par[x] = find(par[x])
    return par[x]

def merger(a, b):
    a, b = find(a), find(b)
    par[min(a,b)] = max(a,b)

def mergel(a, b):
    a, b = find(a), find(b)
    par[a] = b

nums = list(range(1, n+1))
if k == 0:
    print(*nums)
    exit(0)
v = set()
current = k%n
ans = []
while len(ans) < len(nums):
    v.add(current)
    ans.append(nums[current])
    if (current+1)%n in v: mergel(current, (current+1)%n)
    if (current-1)%n in v: merger((current-1)%n-(n if (current-1)%n==n-1 else 0), current)
    cnt = 0
    if len(ans) >= len(nums): break
    steps = k%(n-len(ans))
    if steps == 0: steps += (n-len(ans))
    while cnt <= steps:
        current = (current+1)%n
        if current in v: current = (find(current)+1)%n
        cnt += 1
print(" ".join(map(str, ans)))