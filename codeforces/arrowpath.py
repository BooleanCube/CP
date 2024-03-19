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
    grid = [input(), input()]
    q, vis = deque(), set()
    adj = [1, -1, 0, 0]
    valid = lambda x, y: 0<=x<2 and 0<=y<n
    q.append((0, 0))
    while q:
        cur = q.popleft()
        if cur in vis: continue
        if cur[1] == n-1:
            print("YES")
            return
        vis.add(cur)
        for k in range(4):
            nx, ny = cur[0]+adj[k], cur[1]+adj[-k-1]
            if not valid(nx, ny): continue
            if grid[nx][ny] == ">": ny += 1
            else: ny -= 1
            if (nx, ny) in vis: continue
            q.append((nx, ny))
    print("NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
