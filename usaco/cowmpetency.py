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
    n, q, C = getlist()
    c = getlist(); c[0] = max(c[0], 1)
    zidx = set(i for i in range(n) if c[i] == 0)
    a = sorted([getlist() for _ in range(q)])
    cidx, cmax = 0, c[0]
    for i in range(q):
        aj, hj = a[i]
        hj -= 1; aj -= 1
        for j in range(cidx, aj+1):
            c[j] = max(c[j], 1)
            cmax = max(cmax, c[j])
        if hj in zidx:
            if cmax == C:
                print(-1)
                return
            c[hj] = cmax+1
        elif c[hj] <= cmax:
            print(-1)
            return
    for i in range(n): c[i] = max(c[i], 1)
    print(*c)


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
