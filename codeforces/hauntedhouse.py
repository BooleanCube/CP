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
    b = input()
    ans = []
    pos = [idx for idx in range(n) if b[idx] == "0"]
    c0s = len(pos)
    # print(pos)
    ps = [0]*(c0s+1)
    for i in range(1, c0s+1):
        ps[i] += ps[i-1]+pos[i-1]
    for i in range(1, n+1):
        if i > c0s: ans.append(-1)
        else:
            # print(c0s, c0s-i)
            res = -(ps[c0s]-ps[c0s-i])
            # print(-(ps[c0s]-ps[c0s-i]))
            res += i*(n-i+n-1)//2
            # print(i*(n-i+n-1)//2)
            ans.append(res)
    print(*ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
