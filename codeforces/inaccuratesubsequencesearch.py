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
    n, m, k = getlist()
    a, b = [0]+getlist(), [0]+getlist()
    m1, m2 = Counter(b[1:]), defaultdict(int)
    ans, cur = 0, 0
    for i in range(1, n+1):
        if m2[a[i]] < m1[a[i]]: cur += 1
        m2[a[i]] += 1
        if i >= m+1:
            m2[a[i-m]] -= 1
            if m2[a[i-m]] < m1[a[i-m]]: cur -= 1
        if i >= m and cur >= k: ans += 1
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
