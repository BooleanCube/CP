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
    trees = [tuple(map(int, input().split())) for _ in range(n)]
    treeset = set(trees)
    trees.sort()
    slopes = set()
    for i in range(n):
        for j in range(i+1, n):
            dx, dy = trees[j][0]-trees[i][0], trees[j][1]-trees[i][1]
            g = math.gcd(dx, dy)
            slopes.add((dx//g, dy//g))
    ans = 0
    memo = defaultdict(set)
    for tree in trees:
        x, y = tree
        for dx, dy in slopes:
            pd = 1
            for stree in trees:
                if stree in memo[(dx,dy)]: continue
                nx, ny = stree
                if x==nx and y==ny: continue
                a = abs(nx-x)%abs(dx)==0 and (nx-x)//dx>0 if dx!=0 else nx==x
                b = abs(ny-y)%abs(dy)==0 and (ny-y)//dy>0 if dy!=0 else ny==y
                c = (nx-x)//dx == (ny-y)//dy if dx and dy else True
                if a and b and c: pd += 1; memo[(dx,dy)].add(stree)
            ans = max(ans, pd)
    print(ans)

testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
