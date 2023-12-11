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

segments = []

def good(n, k):
    global segments
    cx, l = 0, -1
    for i in range(n):
        if cx < segments[i][0]:
            if l == 1: cx = segments[i-1][1]
            cx = min(segments[i][1], cx+k)
            l = 0
            if cx < segments[i][0]: return False
        elif cx > segments[i][1]:
            if l == 0: cx = segments[i-1][0]
            cx = max(segments[i][0], cx-k)
            l = 1
            if cx > segments[i][1]: return False
    return True

def solve():
    global segments
    n = getint()
    segments = [tuple(getlist()) for _ in range(n)]
    lo, hi = 0, int(1e9+5)
    while lo<hi:
        m = lo+((hi-lo)>>1)
        if not good(n, m): lo = m+1
        else: hi = m
    for i in range(max(0, lo-10), lo+12):
        if good(n, i):
            print(i)
            break

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
