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
    l = getlist()
    if n == 1: print(1);return
    mx = max(l)
    diffs = []
    for i in range(n):
        diff = mx-l[i]
        if diff: diffs.append(diff)
    x, an1 = math.gcd(*diffs), 0
    s = set(l)
    for i in range(x, int(3e9), x):
        if mx-i not in s:
            an1 = mx-i
            break
    print((sum(diffs)+mx-an1)//x)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
