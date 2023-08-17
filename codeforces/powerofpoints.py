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
    l = [(val, key) for key,val in enumerate(l)]
    ans = [0]*n
    l.sort()
    ans[l[0][1]] = sum(l[i][0]-l[0][0]+1 for i in range(n))
    for i in range(1, n):
        delta = l[i][0]-l[i-1][0]
        ans[l[i][1]] = ans[l[i-1][1]] + delta*i - delta*(n-i)
    print(*ans)
         

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
