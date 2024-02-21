import random
import math
from collections import defaultdict, Counter, deque, OrderedDict
from queue import PriorityQueue
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
from types import GeneratorType
import sys

sys.setrecursionlimit(int(1e5+1e4))

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

edges = defaultdict(list)
vis = set()

def dfs(cur):
    global edges, vis
    if cur in vis: return 0
    vis.add(cur)
    cans, cnt = 0, 0
    for nbr in edges[cur]:
        if nbr in vis: continue
        cans += dfs(nbr)
        cnt += 1
    if cnt == 0: return 0
    return cans/cnt + 1

def solve():
    global edges
    n = getint()
    for _ in range(n-1):
        a, b = getlist()
        edges[a].append(b)
        edges[b].append(a)
    print("%.8f"%(dfs(1)))

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
