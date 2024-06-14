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
    x, y, z, k = getlist()
    dims = []
    for i in range(1, x+1):
        if k % i: continue
        for j in range(1, y+1):
            if i * j > k: break
            if (k // i) % j: continue
            if (k // (i*j)) > z: continue
            dims.append((i, j, k // (i*j)))
    ans = 0
    for dx, dy, dz in dims:
        ans = max(ans, (x-dx+1)*(y-dy+1)*(z-dz+1))
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
