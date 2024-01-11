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
    prefix, suffix = l.copy(), l.copy()
    for i in range(1, n):
        prefix[i] = math.gcd(prefix[i], prefix[i-1])
        suffix[-i-1] = math.gcd(suffix[-i-1], suffix[-i])
    ans = max(suffix[1], prefix[-2])
    for i in range(1, n-1): ans = max(ans, math.gcd(prefix[i-1], suffix[i+1]))
    print(ans)


testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
