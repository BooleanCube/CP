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

def ceil(a, b):
    return a//b + int(a%b>0)

def solve():
    n, m = map(int, input().split())
    p1, p2 = map(int, input().split())
    q1, q2 = map(int, input().split())
    if q2 > p2: p1,p2,q1,q2 = q1,q2,p1,p2
    r1, r2 = p1/p2, q1/q2
    l = list(map(int, input().split()))
    for opp in l:
        if q1>=opp: n-=q2
        elif r1>r2: n-=p2*ceil(opp,p1)
        else: n-=q2*ceil(opp,q1)
    print(["YES", "NO"][n<=0])

testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
