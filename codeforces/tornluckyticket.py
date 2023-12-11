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
    s = input().split()
    s = sorted(s, key=len)
    fq1, fq2, fq3, fq4, fq5 = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    ans = 0
    for i in range(n):
        si = s[i]
        if len(si) == 5:
            sp1 = int(si[0])
            sp2 = sum(int(c) for c in si[:2])
            sp3 = sum(int(c) for c in si[:3])
            sp4 = sum(int(c) for c in si[:4])
            ss1 = int(si[-1])
            ss2 = sum(int(c) for c in si[3:])
            ss3 = sum(int(c) for c in si[2:])
            ss4 = sum(int(c) for c in si[1:])
            sm5 = sum(int(c) for c in si)
            ans += fq1[ss3-sp2] + fq3[ss4-sp1] + fq5[sm5]*2
            ans += fq1[sp3-ss2] + fq3[sp4-ss1]
            fq5[sm5] += 1
        if len(si) == 4:
            sp1 = int(si[0])
            sp3 = sum(int(c) for c in si[:3])
            ss1 = int(si[-1])
            ss3 = sum(int(c) for c in si[1:])
            sm4 = sum(int(c) for c in si)
            ans += fq2[ss3-sp1] + fq4[sm4]*2
            ans += fq2[sp3-ss1]
            fq4[sm4] += 1
        if len(si) == 3:
            sp1 = int(si[0])
            sp2 = sum(int(c) for c in si[:2])
            ss1 = int(si[-1])
            ss2 = sum(int(c) for c in si[1:])
            sm3 = sum(int(c) for c in si)
            ans += fq1[ss2-sp1] + fq3[sm3]*2
            ans += fq1[sp2-ss1]
            fq3[sm3] += 1
        if len(si) == 2:
            sm2 = sum(int(c) for c in si)
            ans += fq2[sm2]*2
            fq2[sm2] += 1
        if len(si) == 1:
            sm1 = int(si[0])
            ans += fq1[sm1]*2
            fq1[sm1] += 1
    print(ans+n)


testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
