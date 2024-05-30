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
    d = input()
    x, y = 0, 0
    for c in d:
        if c == "N": x += 1
        if c == "S": x -= 1
        if c == "E": y += 1
        if c == "W": y -= 1
    if x < 0:
        x = abs(x)
        d = d.replace("N", "T")
        d = d.replace("S", "N")
        d = d.replace("T", "S")
    if y < 0:
        y = abs(y)
        d = d.replace("E", "T")
        d = d.replace("W", "E")
        d = d.replace("T", "W")
    if (x & 1) or (y & 1):
        print("NO")
        return
    ans = ["H"]*n
    gx, gy = x >> 1, y >> 1
    ans[0] = "R"
    if d[0] == "N": gx -= 1
    if d[0] == "S": gx += 1
    if d[0] == "E": gy -= 1
    if d[0] == "W": gy += 1
    for i in range(n):
        if gx > 0 and d[i] == "N":
            ans[i] = "R"
            gx += -1
        if gy > 0 and d[i] == "E":
            ans[i] = "R"
            gy += -1
        if gx < 0 and d[i] == "S":
            ans[i] = "R"
            gx += 1
        if gy < 0 and d[i] == "W":
            ans[i] = "R"
            gy += 1
        if gx == gy == 0: break
    ans = "".join(ans)
    if "H" not in ans:
        print("NO")
        return
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
