import random
import math
from collections import defaultdict, Counter, deque, OrderedDict
from queue import PriorityQueue
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
from re import S
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

cycles = set()

def dfs_cycle(u, p, color, par, edges):
    global cycles
    if color[u] == 2: return
    if color[u] == 1:
        cur = p
        cycles.add(cur)
        while cur != u:
            cur = par[cur]
            cycles.add(cur)
        return
    par[u] = p
    color[u] = 1
    for v in edges[u]:
        if v == par[u]: continue
        dfs_cycle(v, u, color, par, edges)
    color[u] = 2

def solve():
    global cycles
    n, b, a = getlist()
    cycles = set()
    edges = defaultdict(list)
    for _ in range(n):
        f, t = getlist()
        edges[f].append(t)
        edges[t].append(f)

    if b == a:
        print("NO")
        return

    color = [0]*(n+1)
    par = [0]*(n+1)
    dfs_cycle(1, 0, color, par, edges)


    if a in cycles:
        print("YES")
        return

    # find first cycle node
    q = deque()
    q.append((a,0))
    dtc = INF
    cnode = 0
    vis = set()
    while q:
        cur, p = q.popleft()
        vis.add(cur)
        if cur in cycles:
            dtc = p
            cnode = cur
            break
        for v in edges[cur]:
            if v not in vis:
                q.append((v, p+1))

    if dtc == INF:
        print("NO")
        return

    # find how long it takes to reach that node
    q = deque()
    q.append((cnode, 0))
    vis = set()
    ttr = INF
    while q:
        cur, p = q.popleft()
        vis.add(cur)
        if cur == b:
            ttr = p
            break
        for v in edges[cur]:
            if v not in vis:
                q.append((v,p+1))


    print("NO" if ttr <= dtc else "YES")
        

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
