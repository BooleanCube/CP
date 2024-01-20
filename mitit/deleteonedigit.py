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
    s = input()
    if s[-2:] == "11":
        sm = sum(int(c) for c in s)
        if sm % 3 == 0:
            print(s, 3)
        elif sm%3 == 1:
            idx = s.find("1")
            print(s[:idx]+s[idx+1:], 3)
        else:
            idx = s.find("2")
            if idx == -1: print(s[:-1] if len(s)&1 else s, 11)
            else: print(s[:idx]+s[idx+1:], 3)
    elif s[-2:] == "21":
        print(s[:-1], 2)
    else:
        print(s, 2)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
