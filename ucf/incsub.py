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
    if n==1: print(1); return
    m, c = 0, int(l[1]>l[0])
    for i in range(1, n):
        if l[i]>l[i-1]:
            c += 1
        else:
            m = max(m, c)
            c = 1
        m = max(m,c)
    print(m)

testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
