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
    n, m, k = map(int, input().split())
    h = getlist()
    open = PriorityQueue()
    deps = defaultdict(list)
    preqs = defaultdict(set)
    for _ in range(m):
        a,b = getlist()
        deps[a].append(b)
        preqs[b].add(a)
    initset = set(preqs.keys())
    for idx in range(1, n+1):
        if idx not in preqs:
            open.put((h[idx-1], idx))
    first = -1
    mn = float('inf')
    cur = 0
    while not open.empty():
        time, idx = open.get()
        if first == -1: first = time
        base = k*(time//k)
        for dep in deps[idx]:
            preqs[dep].remove(idx)
            if len(preqs[dep]) == 0:
                del preqs[dep]
                ntime, nidx = base+h[dep-1], dep
                open.put((ntime+(k if ntime<time else 0), nidx))
        if idx not in initset and (len(preqs) == 0 or idx > max(preqs.keys())):
            mn = min(mn, cur+k-time)
        cur = time
    print(min(mn, cur-first))


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
