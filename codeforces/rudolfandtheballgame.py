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

def calc(x, d, n, c):
    if c == "1": x = (x - d) % n
    else: x = (x + d) % n
    if x == 0: x = n
    return x

def solve():
    n, m, x = getlist()
    r = [tuple(input().split()) for _ in range(m)]
    tr = []
    for d, t in r:
        d = int(d)
        if t == "?": tr.append(d)
        else: x = calc(x, d, n, t)
    s = set([x])
    for d in tr:
        ns = set()
        for v in s:
            ns.add(calc(v, d, n, "0"))
            ns.add(calc(v, d, n, "1"))
        s = ns
    print(len(s))
    print(*sorted(s))

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
