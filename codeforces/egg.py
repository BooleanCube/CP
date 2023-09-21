from functools import lru_cache
import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

n,f,s = map(int, input().split())
eggs = [tuple(map(int, input().split())) for _ in range(n)]

NINF = -(1e10)

@lru_cache
def dp(idx, f, s):
    if f + s == 0 or idx >= n: return 0
    a = eggs[idx][1] + dp(idx+1, f, s-1) if s>0 else NINF
    b = eggs[idx][0] + dp(idx+1, f-1, s) if f>0 else NINF
    c = dp(idx+1, f, s)
    return max(a,b,c)
    
print(dp(0, f, s))
