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

MAXX = 1000

def solve():
    n = getint()
    s = list(map(int, getstr()))
    fq = defaultdict(int)
    for i in range(n):
        a, b = getlist()
        if s[i]:
            for i in range(b): fq[i] += 1
            for i in range(b+a, MAXX-a, a+a):
                for j in range(i, i+a): fq[j] += 1
        else:
            for i in range(b, MAXX-a, a+a):
                for j in range(i, i+a):
                    fq[j] += 1
    print(max(fq.values()))

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
