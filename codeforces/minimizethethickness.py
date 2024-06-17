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

def thicc(l, j, s, n):
    pi, cs, ans = j, 0, 0
    # print(pi, cs, ans, s, j)
    for i in range(j+1, n):
        cs += l[i]
        if cs > s: return INF
        if cs == s:
            cs = 0
            ans = max(ans, i-pi)
            pi = i
    # print("ans", ans)
    return INF if cs else ans

def solve():
    n, a = getint(), getlist()
    ps, ans = 0, INF
    for i in range(n):
        ps += a[i]
        ans = min(ans, max(i+1, thicc(a, i, ps, n)))
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve() 
