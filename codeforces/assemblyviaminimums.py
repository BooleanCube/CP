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
    b = list(map(int, input().split()))
    f = Counter(b)
    b = sorted(set(b))
    a = []
    for i in range(len(b)):
        a.append(b[i])
        f[b[i]] -= n-len(a)
        while f[b[i]] > 0:
            a.append(b[i])
            f[b[i]] -= n-len(a)
    while len(a)<n: a.append(a[-1])
    print(*a)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
