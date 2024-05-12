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
    l = sorted(getlist())
    v = [0]*n
    ans = [l[-1]]; v[-1] = 1
    pref = ans[0]
    for i in range(min(n-1, int(math.log2(int(1e9)))+3)):
        mxv, mxidx = -1, -1
        for idx in range(n-1, -1, -1):
            if v[idx]: continue
            if (l[idx] | pref) > mxv:
                mxv = (l[idx] | pref)
                mxidx = idx
        ans.append(l[mxidx])
        v[mxidx] = 1
    for i in range(n-1, -1, -1):
        if v[i]: continue
        ans.append(l[i])
    print(*ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
