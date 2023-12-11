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

def ceil(a, b):
    return a//b + int(a%b > 0)

def solve():
    n, P, l, t = getlist()
    print(n-ceil(P, t+t+l))
    nd = n//8+1
    tds = (t+t+l)*(nd//2) + (t+l)*(nd&1)
    otds = (t+l)*nd
    print(nd, tds, ceil(nd, 2), otds, nd, tds/ceil(nd, 2), otds/nd)
    if tds <= P:
        left = P-tds
        print(left)
        print(n-(ceil(nd, 2)+ceil(left, l)))
    else:
        needed = ceil(P, t+t+l)
        print(n-needed)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
