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
MAXN = 2*10**5
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
    if n==1 and l[0]!= 1: print("NO"); return
    d = [l[i-1]-l[i] for i in range(1, n)]
    if l[-1]>n: print("NO"); return
    e = [0]*(l[-1]-1)
    idx = n-1
    while idx > 0:
        p, i = 0, idx
        while i>-1 and l[i] == l[idx]: p+=1; i-=1
        if i < 0: break
        e.append(p)
        if len(e)+l[i]-l[idx]-1 > n: print("NO"); return
        for _ in range(l[i]-l[idx]-1): e.append(0)
        idx = i
    print("YES" if d==e else "NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
