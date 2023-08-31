from collections import defaultdict
import sys

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

n = int(input())
cities = {}
for _ in range(n):
    name, cost = input().split()
    cost = int(cost)
    cities[name] = cost
r = int(input())
conns = defaultdict(list)
for _ in range(r):
    fr, to, mode, p = input().split(); p = int(p)
    conns[fr].append((p, to, mode))
    conns[to].append((p, fr, mode))
start, end = input().split()

ans = float("inf")

def dfs(cur, vis, tprice):
    global ans

    if tprice >= ans: return
    cname, cmode = cur
    if cname in vis: return
    if cname == end: ans = min(ans, tprice); return
    vis.add(cname)
    for conn in conns[cname]:
        price, name, mode = conn
        if name in vis: continue
        if cmode != mode: price += cities[cname]
        dfs((name, mode), vis, tprice+price)
    vis.remove(cname)

v = set([start])
for conn in conns[start]:
    p, name, mode = conn
    dfs((name, mode), v, p)

print(ans)
