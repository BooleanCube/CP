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

def find(l, c):
    for i in range(len(l)):
        if l[i][0] == c:
            return i
    return -1

def rfind(l, c):
    for i in range(len(l)-1, -1, -1):
        if l[i][0] == c:
            return i
    return -1

def solve():
    s = input()
    f, e = s[0], s[-1]
    ss = sorted([(c, i) for i, c in enumerate(s)])
    if f > e: ss = sorted([(c, -i) for i, c in enumerate(s)], reverse=True)
    a, b = find(ss, f), rfind(ss, e)
    print(abs(alp.index(f) - alp.index(e)), (b-a+1))
    print(*[abs(idx)+1 for val, idx in ss[a:b+1]])

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
