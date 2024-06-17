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
    n, m = getlist()
    dic = input().split()
    words = set(dic)
    fq, sub = defaultdict(int), defaultdict(int)
    s = []
    for _ in range(m):
        t = input()[:-1].split()
        for x in t:
            if x in words and (not s or s[-1] != x): s.append(x)
    for i in range(len(s)):
        fq[s[i]] += 1
        if i == 0 or i == len(s)-1: continue
        sub[s[i]] += s[i-1] == s[i+1]
    sm = sum(fq.values())
    for i in range(n):
        print(sm - fq[dic[i]] - sub[dic[i]])

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
