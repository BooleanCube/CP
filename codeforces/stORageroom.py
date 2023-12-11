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
    M = [getlist() for _ in range(n)]
    if n == 1:
        print("YES\n1")
        return
    ans = [0]*n
    for i in range(n):
        ans[i] = min(M[i][:i]+M[i][i+1:])
        for j in range(n):
            if i == j: continue
            ans[i] &= M[i][j]
    NM = []
    for i in range(n):
        NM.append([])
        for j in range(n):
            if i == j: NM[-1].append(0)
            else: NM[-1].append(ans[i] | ans[j])
    if M == NM:
        print("YES")
        print(*ans)
        return
    print("NO")

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
