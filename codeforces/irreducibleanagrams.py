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

A = ord("a")

def solve():
    s = input()
    ps = [tuple([0]*26)]
    for c in s:
        t = list(ps[-1])
        t[ord(c)-A] += 1
        ps.append(tuple(t))
    q = getint()
    for i in range(q):
        l, r = getlist()
        if l == r or s[l-1] != s[r-1]:
            print("Yes")
            continue
        t = [ps[r][j]-ps[l-1][j] for j in range(26)]
        print("Yes" if sum(1 for a in t if a) > 2 else "No")

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
