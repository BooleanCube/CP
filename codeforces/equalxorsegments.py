import random
import math
from collections import defaultdict, Counter, deque, OrderedDict
from queue import PriorityQueue
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right, bisect
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
    n, q = getlist()
    a = getlist()
    px = [0]
    for x in a: px.append(px[-1] ^ x)
    # print(px)
    idxmp = defaultdict(lambda : [-1])
    # idxmp[0].append(0)
    for i, x in enumerate(px): idxmp[x].append(i)
    for v in set(px): idxmp[v].append(n+1)
    for _ in range(q):
        l, r = getlist()
        if px[l-1] == px[r]:
            print("YES")
            continue
        fidx = idxmp[px[l-1]][bisect_left(idxmp[px[l-1]], r) - 1]
        # print(idxmp[px[l-1]], px[l-1], r)
        # print("fidx", fidx)
        if idxmp[px[r]][1] >= fidx:
            print("NO")
            continue
        sidx = idxmp[px[r]][bisect_left(idxmp[px[r]], fidx) - 1]
        if sidx < l:
            print("NO")
            continue
        print("YES")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
