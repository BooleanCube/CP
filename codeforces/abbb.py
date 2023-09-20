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
    s = input()
    vis = set([-1, len(s)])
    i = 0
    while i < len(s)-1:
        if s[i+1] == "B":
            l, r = i, i+1
            while 1:
                vis.add(l); vis.add(r)
                if r+1 in vis or l-1 in vis or s[r+1] != "B": break
                l -= 1; r += 1
            i = r-1
        i += 1
    print(len(s)-len(vis)+2)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
