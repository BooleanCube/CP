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
    a, b = getlist(), getlist()
    m = getint()
    d = getlist()[::-1]
    fixed, miss = set(), defaultdict(int)
    for i in range(n):
        if a[i] == b[i]: fixed.add(a[i])
        else: miss[b[i]] += 1
    if not (d[0] in fixed or d[0] in miss):
        print("NO")
        return
    for i in range(m):
        if d[i] in miss:
            miss[d[i]] -= 1
            if miss[d[i]] == 0:
                del miss[d[i]]
                fixed.add(d[i])
    print("YES" if len(miss) == 0 else "NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
