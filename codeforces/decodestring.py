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

from string import ascii_lowercase as alp

def solve():
    n = getint()
    s = input()
    ans, i = "", 0
    while i < n:
        if i < n-2 and s[i+2] == "0":
            if i < n-3 and s[i+3] == "0":
                ans += alp[int(s[i])-1]
                i += 1
                continue
            ans += alp[int(s[i:i+2])-1]
            i += 3
        elif i < n:
            ans += alp[int(s[i])-1]
            i += 1
    print(ans)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
