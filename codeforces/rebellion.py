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
    z = a.count(0)
    if z == 0:
        print(0)
        return
    idx = "".join(map(str, a)).rfind("0")
    ans = 0
    for i in range(n):
        if z == 0: break
        z -= 1
        if a[i] == 0: continue
        ans += 1
        a[idx] = 1
        while idx >= 0 and a[idx]: idx -= 1
        if idx < 0:
            ans += z
            break
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
