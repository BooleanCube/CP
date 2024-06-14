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
    n, m = getlist()
    a, b = [getlist() for _ in range(n)], [getlist() for _ in range(n)]
    ra, ca = [sorted(row) for row in a], [sorted([a[j][i] for j in range(n)]) for i in range(m)]
    rb, cb = [sorted(row) for row in b], [sorted([b[j][i] for j in range(n)]) for i in range(m)]
    ra.sort(); ca.sort(); rb.sort(); cb.sort()
    print("YES" if ra == rb and ca == cb else "NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
