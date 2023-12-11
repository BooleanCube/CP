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

pow2 = [2**i for i in range(33)]

def solve():
    n = getint()
    b = getlist()
    if n < 2:
        print(0)
        return
    fq = Counter(b)
    ans = 0
    for i in range(n):
        fq[b[i]] -= 1
        if b[i] == 1: ans += fq[1]+fq[2]
        elif b[i] == 2: ans += fq[1]+fq[2]
        else: ans += fq[b[i]]
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
