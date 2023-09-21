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
INF = 1e18
EPS = 1e-9

input = lambda : sys.stdin.readline().strip()
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")
write = lambda *args : sys.stdout.write(" ".join(map(str, args)))

getint = lambda : int(input())
getlist = lambda : list(map(int, input().split()))
getstr = lambda : list(input()) # mutable string

def solve():
    n, x = getlist()
    l = getlist()
    lo, hi = 0, int(INF)
    while lo <= hi:
        mi = (lo+hi)//2
        s = sum(max(0,mi-l[i]) for i in range(n))
        if s > x: hi = mi-1
        elif s < x: lo = mi+1
        else: break
    s, e = max(0,min(lo, hi)-10), max(lo,hi)+10
    for i in range(e, s-1, -1):
        if sum(max(0, i-l[j]) for j in range(n)) <= x:
            print(i)
            break

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
