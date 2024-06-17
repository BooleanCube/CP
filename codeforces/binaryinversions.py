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
    l = getlist()
    pso, psz = [0], [0]
    for i in l:
        pso.append(pso[-1] + i)
        psz.append(psz[-1] + (i^1))
    cur, ans = 0, 0
    for i in range(1, n+1):
        if l[i-1]:
            cur += psz[n] - psz[i]
    for i in range(1, n+1):
        if l[i-1]:
            t = cur - (psz[n] - psz[i])
            t += pso[i-1]
        else:
            t = cur - pso[i-1]
            t += psz[n] - psz[i]
        ans = max(ans, t)
    print(max(ans, cur))

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
