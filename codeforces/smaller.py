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

def query(oa, ob, ca, cb):
    if ob: return 1
    if not oa and ca < cb: return 1
    return 0

def solve():
    oa, ob = 0, 0
    ca, cb = 0, 0
    q = getint()
    for _ in range(q):
        op, k, ss = input().split()
        op, k = int(op), int(k)
        for c in ss:
            if op == 1:
                if c != "a": oa = 1
                else: ca += k
            else:
                if c != "a": ob = 1
                else: cb += k
        print("YES" if query(oa, ob, ca, cb) else "NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
