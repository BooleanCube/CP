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
    a = getlist()
    ans = 1e99
    if n == 1:
        print(0)
        return
    t = a[0]
    l, r = 0, n-1
    while a[l] == t and l<n-1: l += 1
    while a[r] == t and r>0: r -= 1
    ans = min(ans, (0 if r<l else r-l+1))
    t = a[-1]
    l, r = 0, n-1
    while a[l] == t and l<n-1: l += 1
    while a[r] == t and r>0: r -= 1
    ans = min(ans, (0 if r<l else r-l+1))
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
