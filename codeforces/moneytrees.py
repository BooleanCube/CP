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
    n,k = getlist()
    a = getlist()
    h = getlist()
    psum = [0]*(n+1)
    for i in range(1, n+1): psum[i] = psum[i-1]+a[i-1]
    dp = [i for i in range(n)]
    ans = int(a[0] <= k)
    for i in range(1, n):
        if h[i-1]%h[i] == 0 and dp[i-1] != -1:
            dp[i] = dp[i-1]
        while psum[i+1]-psum[dp[i]] > k and dp[i]<i:
            dp[i] += 1
        if dp[i]==i and psum[i+1]-psum[dp[i]] >k:
            dp[i] = -1
        if dp[i] != -1 and psum[i+1]-psum[dp[i]] <= k:
            ans = max(ans, i-dp[i]+1)
    print(ans)


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
