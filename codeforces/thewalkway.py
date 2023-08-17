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
    n, m, d = map(int, input().split())
    b = getlist()
    if b[0] != 1: b = [1] + b
    b.append(n)
    ans = -1
    for i in range(1, len(b)):
        dist = max(b[i]-b[i-1]-1, 0)
        ans += dist//d+1
    c = 0
    for i in range(1, len(b)-1):
        l, cur, u = b[i-1], b[i], b[i+1]
        if cur == u: c += int(0 < (cur-l)%d); continue
        if (u-cur-1)//d+(cur-l-1)//d+2 > (u-l-int(i+1!=m+1))//d+1: c += 1
    if c: print(ans, c)
    else: print(ans+1, m)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
