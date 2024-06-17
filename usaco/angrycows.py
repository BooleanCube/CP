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

sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")

input = lambda : sys.stdin.readline().strip()
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")
write = lambda *args : sys.stdout.write(" ".join(map(str, args)))

getint = lambda : int(input())
getlist = lambda : list(map(int, input().split()))
getstr = lambda : list(input()) # mutable string

def good(R, r=0):
    for l in range(n):
        f = int(x[r] - x[l] <= 2*R)
        while r < n and x[r] - x[l] <= 2*R: r += 1
        r -= f
        if max(pref[l], suff[r]) <= R - 1: return 1
    return 0

n = getint()
x = sorted(set([getint() for _ in range(n)]))
n = len(x)
t = (x[0] + x[-1]) / 2

pref, suff = [INF]*n, [INF]*n
pref[0] = suff[-1] = 0
pidx, sidx = 0, n-1
for i in range(1, n):
    while pidx+1 < i and x[i] - x[pidx+1] > pref[pidx+1]+1: pidx += 1
    pref[i] = min(x[i] - x[pidx], pref[pidx+1]+1)
    while sidx-1 > (n-i-1) and x[sidx-1] - x[-i-1] > suff[sidx-1]+1: sidx -= 1
    suff[-i-1] = min(x[sidx] - x[-i-1], suff[sidx-1]+1)

lo, hi = 0, 1e9
for _ in range(100):
    mid = lo + (hi - lo) / 2
    if good(mid): hi = mid
    else: lo = mid
print("%.1f" % lo)
