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
    n, q = getlist()
    a = getlist()
    x = getlist()
    mp = defaultdict(list)
    for idx in range(n):
        b = bin(a[idx])[2:]
        m = len(b)
        mp[m-b.rfind("1")-1].append(idx)
    for p in x:
        nl = []
        for o in range(p, 33):
            for idx in mp[o]:
                a[idx] += (1 << (p-1))
                nl.append(idx)
            del mp[o]
        if len(nl): mp[p-1] += nl
    print(*a)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
