#MLE on tc6

from bisect import bisect_right

MOD = 998244353

n = int(input())
p, xs = {}, []
for i in range(n):
    x, y, a = map(int, input().split())
    p[x] = (y, a)
    xs.append(x)

xs.sort()
dp = [0]*(n+1)
cur, ans = 0, xs[-1]+1
while cur < xs[-1]:
    pidx = bisect_right(xs, cur)
    next = xs[pidx]
    ncur = p[next][0]
    npidx = bisect_right(xs, ncur-1)
    nnext = xs[npidx]
    step = next-ncur+dp[pidx]-dp[npidx]
    if p[next][1]: ans += step
    dp[pidx+1] = step+dp[pidx]
    cur = next; ans %= MOD

print(ans)
