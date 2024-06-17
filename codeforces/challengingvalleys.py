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

def remdup(l):
    a = [l[0]]
    for i in l:
        if i == a[-1]: continue
        a.append(i)
    return a

def solve():
    n = getint()
    l = getlist()
    l = remdup(l)
    n = len(l)
    if n == 1:
        print("YES")
        return
    a = sum(l[i-1] > l[i] < l[i+1] for i in range(1, n-1))
    a += l[0] < l[1]
    a += l[-2] > l[-1]
    print("NO" if a > 1 else "YES")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
