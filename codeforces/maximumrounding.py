import random
from math import floor, log10
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

def rounds(x, sig):
    return round(x, sig-int(floor(log10(abs(x))))-1)

def solve():
    n = [0]+list(map(int, input()))
    f = Counter(n)
    m = len(n)
    i = m-1
    while i>0:
        a = sum(f[j] for j in range(5, 10))
        if a == 0: break
        o = i
        e = 1
        if n[i] >= 5:
            f[n[i-1]] -= 1
            n[i-1] += 1
            while n[i-1] > 9:
                f[n[i-2]] -= 1
                n[i-2] += 1
                f[n[i-2]] += 1
                n[i-1] = 0
                f[0] += 1
                i -= 1
                e = 0
            if e: f[n[i-1]] += 1
        f[n[o]] -= 1
        n[o] = 0
        if e: i -= 1
    print(int("".join(map(str, n))))

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
