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
    n, q = getlist()
    grid = [[[[], defaultdict(int)] for _ in range(n)] for _ in range(n)]
    for _ in range(q):
        line = input().split()
        op = int(line[0])
        if op == 0:
            l, x, y = line[1], int(line[2]), int(line[3])
            grid[x][y][0].append(l)
            grid[x][y][1][l] += 1
        if op == 1:
            x, y = map(int, line[1:])
            l = grid[x][y][0].pop(-1)
            grid[x][y][1][l] -= 1
        if op == 2:
            l, x, y = line[1], int(line[2]), int(line[3])
            print("yes" if grid[x][y][1][l] > (len(grid[x][y][0]) / 2) else "no")

testcases = 1
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
