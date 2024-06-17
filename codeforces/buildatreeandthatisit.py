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
    n, d12, d23, d31 = getlist()
    x, y, z = d12+d31-d23, d12+d23-d31, d23+d31-d12
    l = [x, y, z]
    if x+y+z > ((n-1)<<1) or any([(c&1) for c in l]) or any([c<0 for c in l]):
        print("NO")
        return
    print("YES")
    x, y, z = (x>>1), (y>>1), (z>>1)
    l = [0, x, y, z]
    # print(l)
    s = list(range(4, n+1))
    edges = []
    root = n
    for i in range(1, 4):
        if l[i] == 0: root = i
    if root == n and root > 3: s.pop(-1)
    for i in range(1, 4):
        cur = root
        for _ in range(0, l[i]-1):
            nbr = s.pop(-1)
            edges.append((cur, nbr))
            cur = nbr
        if l[i]: edges.append((i, cur))
    for r in s: edges.append((1, r))
    for u, v in edges: print(u, v)


testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
