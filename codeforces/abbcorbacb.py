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
    s = getstr()
    n = len(s)
    idx = [i for i in range(n) if s[i] == "B"]
    vis = set()
    cas = []
    if idx[0] > 0: cas.append((idx[0], 0, idx[0]-1))
    if idx[-1] < n-1: cas.append((n-1-idx[-1], idx[-1]+1, n-1))
    for b in range(1, len(idx)):
        cas.append((idx[b]-idx[b-1]-1, idx[b-1]+1, idx[b]-1))
    cas.sort(reverse=True) 


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
