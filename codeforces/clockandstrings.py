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
    a,b,c,d = getlist()
    a -= 1; b-= 1; c -= 1; d -= 1
    a, b = min(a,b), max(a,b)
    c, d = min(c,d), max(c,d)
    l, r = set(), set()
    lp, rp = a, a
    while lp != b:
        lp -= 1
        lp %= 12
        l.add(lp)
    while rp != b:
        rp += 1
        rp %= 12
        r.add(rp)
    if (c in l and d in r) or (d in l and c in r):
        print("YES")
        return
    print("NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
