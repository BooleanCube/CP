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
    n, k, q = getlist()
    a, b = [0] + getlist(), [0] + getlist()
    ans = []
    for _ in range(q):
        d = getint()
        if d == n:
            ans.append(b[-1])
            continue
        idx = bisect_right(a, d) - 1
        s = (a[idx+1] - a[idx]) / (b[idx+1] - b[idx])
        t = int((d - a[idx])/s + b[idx])
        ans.append(t)
    print(*ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
