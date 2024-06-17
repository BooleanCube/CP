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


def binsearchv2(n, x, tx, p):
    l, r = 1, n+1
    ans = []
    while 1:
        if r - l == 1: break
        m = (l + r) // 2
        if m <= tx:
            if p[m] > x: ans.append((m, 0))
            l = m
        else:
            if p[m] <= x: ans.append((m, 1))
            r = m
    return ans

def binsearch(n, x, p):
    l, r = 1, n+1
    idx = set()
    while 1:
        if r - l == 1: break
        m = (l + r) // 2
        idx.add(m)
        if p[m] <= x: l = m
        else: r = m
    return l, idx

def verify(n, x, p):
    l, r = 1, n+1
    while 1:
        if r - l: break
        m = (l + r) // 2
        if p[m] <= x: l = m
        else: r = m
    return p[l] == x

def swap1(tidx, xidx):
    print(1)
    print(tidx, xidx)

def findbelow(x, idxmp, inds):
    for r in range(1, x):
        if idxmp[r] not in inds:
            return idxmp[r]
    return -1

def findabove(x, idxmp, inds, p):
    n = len(idxmp)
    r = [i for i in range(x+1, n+1) if idxmp[i] not in inds][0]
    p[idxmp[r]], p[idxmp[x]] = p[idxmp[x]], p[idxmp[r]]
    l, ch = binsearch(n, x, p)
    p[idxmp[r]], p[idxmp[x]] = p[idxmp[x]], p[idxmp[r]]
    return l, [idxmp[i] for i in range(x+1, n+1) if idxmp[i] not in ch][0]

def swap2(x, idxmp, inds, p):
    r = findbelow(x, idxmp, inds)
    if r != -1:
        print(2)
        print(idxmp[x], r)
        return
    t, r = findabove(x, idxmp, inds, p)
    return

def solve():
    n, x = map(int, input().split())
    perm = list(map(int, input().split()))
    P = 0
    for i in range(n):
        if perm[i] == x: P = i
    l, r = 0, n
    while r - l > 1:
        m = (l + r) // 2
        if perm[m] <= x: l = m
        else: r = m

    print("1")
    print(P + 1, l + 1)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
