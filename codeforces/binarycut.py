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

def geninds(s):
    ans = []
    for i in range(len(s)-1):
        if s[i] == "1" and s[i+1] == "0":
            ans.append(i+1)
    return ans

def solve():
    s = input()
    l = []
    p, cur = s[0], 1
    for i in range(1, len(s)):
        if s[i] == p: continue
        l.append((p, cur))
        cur, p = 1, s[i]
    l.append((p, cur))
    f = 0
    for i in range(len(l)-1):
        if l[i][0] == "0" and l[i+1][0] == "1":
            f = 1
    print(len(l)-f)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
