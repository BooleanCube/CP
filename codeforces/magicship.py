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
    mv = "UDLR"
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    d = []
    d.append((0, 0))
    st = tuple(map(int, input().split()))
    fi = tuple(map(int, input().split()))
    n = int(input())
    s = input()
    for i in range(n):
        id = mv.find(s[i])
        assert id != -1
        d.append((d[i][0] + dx[id], d[i][1] + dy[id]))
    lo, hi = 0, 10**18
    while hi - lo > 1:
        mid = lo+(hi-lo)//2
        cnt, r = mid//n, mid%n
        cx = st[0] + d[r][0] + cnt*d[n][0]
        cy = st[1] + d[r][1] + cnt*d[n][1]
        dist = abs(cx-fi[0]) + abs(cy-fi[1])
        if dist <= mid: hi = mid
        else: lo = mid
    if hi > 5e17:
        hi = -1
    print(hi)

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
