# TLE on tc 22

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
    _, k = map(int, input().split())
    l = getlist()
    f = Counter(l)
    l = sorted(set(l))
    m, c, s, flag = 0, 0, -1, int(f[l[0]] < k)
    if flag == 0: s = l[0]
    for i in range(1, len(l)):
        if f[l[i]] >= k:
            flag = 0
            if s == -1: s = l[i]
        if l[i] == l[i-1]+1 and f[l[i]] >= k and f[l[i-1]] >= k:
            c += 1
        else:
            if c > m:
                m = c
                s = l[i-1]-c
            c = 0
    if c > m:
        m = c
        s = l[-1]-c
    if flag: print(-1)
    else: print(s, s+m)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
