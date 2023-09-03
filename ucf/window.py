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
    n, k = map(int, input().split())
    l = [getint() for _ in range(n)]
    ps = [0]*(n+1)
    for i in range(1, n+1):
        ps[i] = ps[i-1]+l[i-1]
    ans = []
    cs = sum((i+1)*l[i] for i in range(k))
    ans.append((cs, 1))
    for i in range(1, n-k+1):
        cs -= ps[i+k-1]-ps[i-1]
        cs += l[i+k-1]*k
        ans.append((cs, i+1))
    ans.sort()
    for s in ans:
        sm, idx = s
        print(idx, sm)

testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
