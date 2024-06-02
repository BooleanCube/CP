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


def dfs(u, p, par, graph):
    par[u] = p
    for v in graph[u]:
        if v == p :continue
        dfs(v, u, par, graph)

def solve():
    n = getint()
    r = getlist()
    par = [0]*n
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = getlist()
        a -= 1; b -= 1
        graph[a].append(b)
        graph[b].append(a)
    dfs(0, 0, par, graph)
    vis = [0]*n
    for i in range(1, n):
        if r[i] >= r[0]:
            j = i
            while j and par[j]:
                if vis[par[j]]: break
                j = par[j]
                vis[j] = 1
    print(sum(vis))

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
