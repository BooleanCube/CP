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
    ans, f = 0, min(abs(x-b[-1]) for x in a+b[:-1])+1
    for i in range(n):
        if b[i] == b[-1]: f = 1
        if a[i] == b[i]: continue
        elif a[i] > b[i]:
            if a[i] >= b[-1] >= b[i]: f = 1
            ans += a[i] - b[i]
        else:
            if a[i] <= b[-1] <= b[i]: f = 1
            ans += b[i] - a[i]
    print(ans + f)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
