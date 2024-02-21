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

def cntlz(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] != "0": break
        cnt += 1
    return cnt

def solve():
    n, m = getlist()
    l = input().split()
    lz = [cntlz(l[i][::-1]) for i in range(n)]
    lz.sort(reverse=True)
    cnt = 0
    for i in range(n):
        cnt += len(l[i])
    zr = sum(lz[0::2])
    print(("Sasha" if cnt-zr >= m+1 else "Anna"))

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
