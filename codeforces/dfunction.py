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


def fastexpo(b, e):
    if e == 0: return 1
    if e == 1: return b % MOD
    t = (fastexpo(b, e>>1) ** 2) % MOD
    if e & 1: return (b * t) % MOD
    return t

def invmod(i):
    if i == 1: return 1
    return (MOD - ((MOD//i) * invmod(MOD % i)) % MOD + MOD) % MOD

def geomseries(r, n):
    if n < 0: return 0
    return ((fastexpo(r, n+1) - 1) * invmod(r - 1)) % MOD

def geomseriesrng(d, l, r):
    return (geomseries(d, r-1) - geomseries(d, l-1)) % MOD

def solve():
    l, r, k = getlist()
    d = 9 // k
    if d == 0:
        print(0)
        return
    ans = (d * geomseriesrng(d+1, l, r)) % MOD
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
