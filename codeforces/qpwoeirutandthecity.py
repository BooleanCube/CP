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
    n = int(input())
    h = getlist()
    if n&1:
        print(sum(max(h[i-1], h[i+1], h[i]-1)-h[i]+1 for i in range(1, n, 2)))
    else:
        vis = set([0, n-1])
        a = [max(h[i-1], h[i+1], h[i]-1)-h[i]+1 for i in range(1, n-1, 2)]
        b = [max(h[i-1], h[i+1], h[i]-1)-h[i]+1 for i in range(2, n, 2)]
        psa = [0]*(len(a)+1)
        psb = [0]*(len(b)+1)
        for i in range(1, len(a)+1): psa[i] = psa[i-1]+a[i-1]
        for i in range(1, len(b)+1): psb[i] = psb[i-1]+b[i-1]
        ans = INF
        for i in range(len(a)+1):
            ans = min(ans, psa[i]-psa[0] + psb[-1]-psb[i])
        print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
