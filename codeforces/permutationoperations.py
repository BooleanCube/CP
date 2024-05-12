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
    p = getlist()[::-1]
    ans, cnt, ops = [], 1, 0
    for i in range(1, n):
        if p[i] > p[i-1]:
            diff = p[i] - p[i-1]
            while diff > 0:
                diff -= cnt
                ans.append(n-i+1)
                cnt += 1; ops += 1
    for _ in range(n - ops): ans.append(1)
    print(*ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
