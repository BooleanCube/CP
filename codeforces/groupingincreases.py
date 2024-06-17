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
    rda = [a[0]]
    for i in range(1, n):
        if rda[-1] == a[i]: continue
        rda.append(a[i])
    a = rda
    n = len(a)
    acnt = 0
    for i in range(n-1): acnt += a[i] < a[i+1]
    b, bcnt, ans = [], 0, acnt
    for i in range(n-1):
        if a[i] < a[i+1]:
            if i == 0 or (a[i-1] >= a[i+1]): acnt -= 1
            b.append(a[i])
            if len(b) > 1 and b[-1] > b[-2]: bcnt += 1
            ans = min(ans, acnt + bcnt)
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
