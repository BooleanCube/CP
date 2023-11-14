from math import comb
from functools import cache

ans = 0

@cache
def dp(cf, ff, exp, chp):
    global ans
    if cf == 0 and ff == 0:
        ans += 1
        return
    if exp: dp(cf-1, ff, exp-1, chp)
    if chp: dp(cf, ff-1, exp, chp-1)
    if exp: dp(cf, ff-1, exp-1, chp)
    

tc = int(input())

for _ in range(tc):
    n, m, k, d = map(int, input().split())
    l = list(map(int, input().split()))
    e = len([a for a in l if a >= d])
    ans = 0
    dp(k, n-k, e, n-e)
    print(ans)