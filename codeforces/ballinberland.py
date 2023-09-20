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
    a, b, k = map(int, input().split())
    freqb = defaultdict(int)
    freqg = defaultdict(int)
    a = getlist()
    b = getlist()
    for boy,girl in zip(a,b):
        freqb[boy] += 1
        freqg[girl] += 1
    ans = 0
    for eb, eg in zip(a,b): ans += k-(freqb[eb]+freqg[eg]-1)
    print(ans//2)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
