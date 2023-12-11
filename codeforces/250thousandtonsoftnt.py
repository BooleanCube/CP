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
    a = getlist()
    psum = [0]
    for i in a: psum.append(i+psum[-1])
    ans = 0
    for k in range(1, n):
        if n%k > 0: continue
        mn, mx, cnt = 1e20, 0, 0
        for i in range(k, n+1, k):
            mn = min(mn, psum[i]-psum[i-k])
            mx = max(mx, psum[i]-psum[i-k])
            cnt += 1
        if cnt == 1: break
        ans = max(ans, mx-mn)
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
