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
    a = list(map(int, getstr()))
    ps = [0]
    for i in a: ps.append(ps[-1] + i)
    awt, aidx, = 1e99, 0
    for i in range(n+1):
        l, r = (i - ps[i]), (ps[-1]-ps[i])
        wt = abs((n / 2) - i)
        # print(n, i, wt, l, r)
        if l >= (i+1)//2 and r >= (n-i+1)//2 and wt < awt: awt, aidx = wt, i
    print(aidx)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
