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
    n, m = map(int, input().split())
    grid = [getstr() for _ in range(n)]
    poss = 1
    for i in grid:
        if (m-i.count("."))&1: poss=0
    for i in range(m):
        l = [grid[j][i] for j in range(n)]
        if (n-l.count("."))&1: poss=0
    if not poss: print(-1); return
    for i in range(n-1):
        last = 0
        for j in range(m):
            if grid[i][j] == "U":
                grid[i][j] = "WB"[last]
                grid[i+1][j] = "BW"[last]
                last = not last
    for i in range(m-1):
        last = 0
        for j in range(n):
            if grid[j][i] == "L":
                grid[j][i] = "WB"[last]
                grid[j][i+1] = "BW"[last]
                last = not last
    for row in grid:
        print("".join(row))


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
