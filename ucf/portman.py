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
    a = getstr()
    b = getstr()
    l, r = a[0], b[-1]
    v1, v2 = "",""
    for c in a[1:]:
        if c in "aeiou":
            v1 = c
            break
        l += c
    for c in b[:-1][::-1]:
        if c in "aeiou":
            v2 = c
            break
        r += c
    ans = l+(v2 if v2!="" else v1 if v1 != "" else "o")+r[::-1]
    print(ans)

testcases = 1
#testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
