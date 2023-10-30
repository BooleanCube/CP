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
    l = sorted(getlist())
    x = 0
    lp, rp = 0, n-1
    ans = 0
    while lp<rp:
        target = l[rp]
        if x+l[lp] <= target:
            x += l[lp]
            ans += l[lp]
            l[lp] = 0
            lp += 1
        elif x+l[lp] > target:
            val = target - x
            x += val
            ans += val
            l[lp] -= val
        if x == target:
            x = 0
            l[rp] = 0
            ans += 1
            rp -= 1
    while lp==rp and l[lp] > 0:
        a = (l[rp]-x)//2
        if a == 0:
            if x > 0:
                ans += 1
                l[rp] -= x
                x = 0
            ans += l[rp]
            l[rp] = 0
            break
        x += a
        l[rp] -= a+x
        ans += a+1
        x = 0
    print(ans)


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
