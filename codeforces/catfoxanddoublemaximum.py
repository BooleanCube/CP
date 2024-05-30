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

def isolve(a, f, s):
    n = len(a)
    if f[0][1] & 1:
        f.append((int(INF), n-1))
        s.append((a[0], 0))
    else:
        f.append((int(INF), 0))
        s.append((a[-1], -1))
    s.sort()
    ans = [0] * n
    for i in range(n >> 1): ans[f[i][1]] = n - i
    for i in range(n >> 1): ans[s[i][1]] = (n >> 1) - i
    l = [x+y for x, y in zip(a, ans)]
    return (sum(l[i-1]<l[i]>l[i+1] for i in range(1, n-1)), ans)

def solve():
    n = getint()
    a = getlist()
    f, s = sorted((a[i], i) for i in range(2, n, 2)), sorted((a[i], i) for i in range(1, n-1, 2))
    print(*max(isolve(a, f, s), isolve(a, s, f))[1])
    # print(*[x+y for x, y in zip(a, ans)])

testcases = 1
testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
