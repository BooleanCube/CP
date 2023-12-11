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
    x1, y1, x2, y2, x3, y3 = getlist()
    area = x1*y1 + x2*y2 + x3*y3
    side = math.isqrt(area)
    if side*side != area:
        print(-1)
        return
    grid = [[""]*side for _ in range(side)]
    if x1 > side or y1 > side:
        print(-1)
        return
    if y1 > x1: x1, y1 = y1, x1
    for i in range(y1):
        for j in range(x1):
            grid[i][j] = "A"
    mx, my, mc = -1, -1, ""
    if x1 < side:
        rem = side-x1
        x2, y2 = min(x2, y2), max(x2, y2)
        x3, y3 = min(x3, y3), max(x3, y3)
        if x2 <= rem:
            for i in range(x1, x1+x2):
                for j in range(y2):
                    grid[i][j] = "B"
            mx, my, mc = x3, y3, "C"
        elif x3 <= rem:
            for i in range(x1, x1+x3):
                for j in range(y3):
                    grid[i][j] = "C"
            mx, my, mc = x2, y2, "B"
        else:
            print(-1)
            return
    else:
        rem = side-y1
        y2, x2 = min(x2, y2), max(x2, y2)
        y3, x3 = min(x3, y3), max(x3, y3)
        if y2 <= rem:
            for i in range(y1, y1+y2):
                for j in range(x2):
                    grid[i][j] = "B"
            mx, my, mc = x3, y3, "C"
        elif y3 <= rem:
            for i in range(y1, y1+y3):
                for j in range(y3):
                    grid[i][j] = "C"
            mx, my, mc = x2, y2, "B"
        else:
            print(-1)
            return
    tl, br = (-1, -1), (0, 0)
    for i in range(side):
        for j in range(side):
            if grid[i][j] == "" and tl == (-1, -1):
                tl = (i, j)
            if grid[i][j] == "":
                br = (i+1, j+1)
    rx, ry = br[0]-tl[0], br[1]-tl[1]
    if min(mx, my) == min(rx, ry) and max(mx, my) == max(rx, ry):
        for i in range(tl[0], br[0]):
            for j in range(tl[1], br[1]):
                grid[i][j] = mc
    else:
        print(-1)
        return
    print(side)
    for row in grid:
        print("".join(row))

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
