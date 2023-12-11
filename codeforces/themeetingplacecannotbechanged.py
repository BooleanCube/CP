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

def solve():
    n = getint()
    x = getlist()
    v = getlist()
    lo, hi, ans = 0, int(1e9+5), 0
    for _ in range(100):
        mid1 = lo+(hi-lo)/2
        mid2 = mid1+1e-6
        t1, t2 = 0, 0
        for i in range(n):
            t1 = max(t1, abs(x[i]-mid1)/v[i])
            t2 = max(t2, abs(x[i]-mid2)/v[i])
        if t1 > t2: lo = mid2; ans = t2
        else: hi = mid1; ans = t1
    print("%.8f"%ans)

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
