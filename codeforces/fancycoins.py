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
    m, k, ao, ak = map(int,input().split())
    if k*ak>m and ao<m%k: print(m%k-ao); return
    if k*ak+ao >= m: print(0); return
    ans = m-ak*k-ao
    start = max(0,(m-ao)//k-100)
    end = start + 200
    for i in range(start, end):
        if i<=ak: continue
        if i*k > m: break
        ans = min(ans, i-ak + max(0, m-i*k-ao))
    print(ans)



testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
