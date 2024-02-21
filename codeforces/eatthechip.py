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
    h, w, xa, ya, xb, yb = getlist()
    if xa >= xb:
        print("Draw")
        return
    if (xb-xa)&1:
        # alice can win
        insta = xb-xa-1 <= 2 and abs(yb-ya) <= 1 or w <= 3
        run = w - yb if ya < yb else 0 if ya == yb else yb - 1
        reach = xb-xa-1 >= abs(yb-ya)+run
        print("Draw" if not reach and not insta else "Alice")
    else:
        # bob can win
        insta = xb-xa-1 <= 2 and abs(yb-ya) <= 1 or w <= 3
        run = w - ya if yb < ya else 0 if ya == yb else ya - 1
        reach = xb-xa-1 > abs(yb-ya)+run
        print("Draw" if not reach and not insta else "Bob")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
