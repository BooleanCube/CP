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
EPS = 1e-6

input = lambda : sys.stdin.readline().strip()
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")
write = lambda *args : sys.stdout.write(" ".join(map(str, args)))

getint = lambda : int(input())
getlist = lambda : list(map(int, input().split()))
getstr = lambda : list(input()) # mutable string

def area(pts):
    n = len(pts)
    area = 0
    for i in range(n):
        j = (i+1)%n
        area += pts[i][0]*pts[j][1] - pts[j][0]*pts[i][1]
    return abs(area)/2

def angle(pt, cent):
    return -math.atan2(pt[1]-cent[1], pt[0]-cent[0])

def solve():
    n = getint()
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    center = (sum(pt[0] for pt in pts)/n, sum(pt[1] for pt in pts)/n)
    pts.sort(key=lambda pt: angle(pt, center))
    ans = INF
    for i in range(n):
        for j in range(i+2, i+2+n-2):
            d = j-i+1
            s1 = [pts[k%n] for k in range(i, j+1)]
            s2 = [pts[k%n] for k in range(j, i+1+(n if i<j else 0))]
            ans = min(ans, abs(area(s1)-area(s2)))
    print(round(ans, 1))

testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
