from bisect import bisect_left

def cmpleeq(a,b):
    return -1 if a>b else 1

def cmple(a,b):
    return -1 if a>=b else 1

def first_leeq(arr,target,cmp):
    i,j = 0,len(arr)-1
    while i < j:
        m = i + (j-i) // 2
        if cmp(arr[m], target) >= 0:
            j = m
        else:
            i = m + 1
    if cmp(arr[i], target) < 0: return i + 1
    return i

n = int(input())
x, h = [], []
for i in range(n):
    xi,hi = map(int,input().split())
    x.append(xi); h.append(hi)

dp = [0]*n
indices = [n-1]
dp[n-1] = 1

for i in range(n-2, -1, -1):
    idx = bisect_left(x, x[i]+h[i]+1)-1
    if i == idx:
        dp[i] = 1
        indices.append(i)
        continue
    ridx = indices[first_leeq(indices, idx, cmpleeq)]
    dp[i] = dp[ridx]+ridx-i
    while indices and dp[indices[-1]]+indices[-1]-i-1 <= dp[i]:
        indices.pop(-1)
    indices.append(i)

print(*dp)
