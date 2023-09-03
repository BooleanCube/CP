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

ans = INF

def dfs(areas, pts):
    global ans
    if len(areas) > 0 and max(areas)-min(areas) >= ans: return
    if len(pts) == 0:
        ans = min(ans, max(areas)-min(areas))
    else:
        for a in range(len(pts)):
            for b in range(a+1, len(pts)):
                for c in range(b+1, len(pts)):
                    pa, pb, pc = pts[a], pts[b], pts[c]
                    sa = math.dist(pa, pb)
                    sb = math.dist(pb, pc)
                    sc = math.dist(pc, pa)
                    if sc>=sa+sb or sb>=sa+sc or sa>=sb+sc: continue
                    pts.pop(a); pts.pop(b-1); pts.pop(c-2)
                    s = (sa+sb+sc)/2
                    area = math.sqrt(s*(s-sa)*(s-sb)*(s-sc))
                    dfs(areas+[area], pts)
                    pts.insert(a, pa); pts.insert(b, pb); pts.insert(c, pc)


def solve():
    n = getint()
    points = [tuple(map(int, input().split())) for _ in range(3*n)]
    dfs([], points)
    print(round(ans, 1))

testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
