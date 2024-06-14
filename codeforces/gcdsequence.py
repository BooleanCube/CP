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
    a = getlist()
    g = [math.gcd(a[i-1], a[i]) for i in range(1, n)]
    idx = [i for i in range(1, len(g)) if g[i] < g[i-1]]
    if not idx:
        print("YES")
        return
    idx = idx[0] + 1
    # print(idx)
    if idx > 1:
        x = a[:idx-2] + a[idx-1:]
        # print(x)
        x = [math.gcd(x[i-1], x[i]) for i in range(1, n-1)]
        # print(x)
        if x == sorted(x):
            print("YES")
            return
    y, z = a[:idx] + a[idx+1:], a[:idx-1] + a[idx:]
    # print(y, z)
    y, z = [math.gcd(y[i-1], y[i]) for i in range(1, n-1)], [math.gcd(z[i-1], z[i]) for i in range(1, n-1)]
    # print(y, z)
    print("YES" if y == sorted(y) or z == sorted(z) else "NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
