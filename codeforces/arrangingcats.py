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
    s, f = getstr(), getstr()
    onp = sum(1 for i in range(n) if int(s[i]) and int(f[i])==0)
    enp = sum(1 for i in range(n) if int(s[i])==0 and int(f[i]))
    ops = 0
    if onp >= enp:
        onp -= enp
        ops += enp
        enp = 0
    else:
        enp -= onp
        ops += onp
        onp = 0
    print(onp+enp+ops)

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
