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
MAXN = 10**6+5
INF = 1e20
EPS = 1e-9

input = lambda : sys.stdin.readline().strip()
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")
write = lambda *args : sys.stdout.write(" ".join(map(str, args)))

getint = lambda : int(input())
getlist = lambda : list(map(int, input().split()))
getstr = lambda : list(input()) # mutable string


def modinv(i):
    if i == 1: return 1
    return (MOD - (((MOD//i)*modinv(MOD%i))%MOD)+MOD) % MOD

def fastexpo(a, b):
    if b == 0: return 1
    if b == 1: return a % MOD
    temp = (fastexpo(a, b>>1) ** 2) % MOD
    if b&1: return (temp * a) % MOD
    return temp

def solve():
    n, k = getlist()
    s = input()
    ans = 1
    for i in range(k):
        d = Counter(s[i::k])
        cur = fact[sum(d.values())]
        for x in d:
            cur *= modinv(fact[d[x]])
            cur %= MOD
        ans *= cur
        ans %= MOD
    print(ans)

fact = [0]*MAXN
fact[0] = fact[1] = 1
for i in range(2, MAXN): fact[i] = (fact[i-1]*i) % MOD

testcases = 1
# testcases = getint()
for c in range(1, testcases+1):
    #write(f"Case {c}: ")
    solve()
