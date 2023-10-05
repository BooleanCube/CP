import random
import math
from collections import defaultdict, Counter, deque, OrderedDict
from queue import PriorityQueue
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
from types import GeneratorType
import sys

MOD = 10**9+7
HMOD = 998244353
MAXN = 10**5+5
INF = 1e20
EPS = 1e-9

input = lambda : sys.stdin.readline().strip()
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")
write = lambda *args : sys.stdout.write(" ".join(map(str, args)))

getint = lambda : int(input())
getlist = lambda : list(map(int, input().split()))
getstr = lambda : list(input()) # mutable string

def query(ps, l, r):
    ans = 0
    for i in range(32):
        x = ps[i][r] if l==0 else ps[i][r]-ps[i][l-1]
        if x == r-l+1:
            ans |= 1<<i
    return ans

def solve():
    n = getint()
    l = getlist()
    ps = [[0]*(n+1) for _ in range(32)]
    for i in range(32):
        ps[i][0] = (l[0] >> i) & 1
        for j in range(1, n):
            ps[i][j] = (l[j] >> i) & 1
            ps[i][j] += ps[i][j-1]
    q = getint()
    ans = []
    for i in range(q):
        l, k = getlist()
        l -= 1
        lo, hi = l, n-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            res = query(ps, l, mid)
            if res < k: hi = mid-1
            else: lo = mid+1
        ans.append(hi+1 if hi>=l else -1)
    print(*ans)


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
