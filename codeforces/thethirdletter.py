import sys

input = sys.stdin.readline
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")

N = int(2e5+5)
adj = [[] for _ in range(N)]
vis, val = [0]*N, [0]*N

def dfs(u):
    if vis[u]: return
    stack = []; stack.append(u)
    while stack:
        c = stack.pop(-1)
        if vis[c]: continue
        vis[c] = 1
        for v, w in adj[c]:
            if vis[v]: continue
            val[v] = val[c] + w
            stack.append(v)

for _ in range(int(input())):
    n, m = map(int, input().split())
    for i in range(1, n+5):
        adj[i] = []
        vis[i], val[i] = 0, 0
    c = [tuple(map(int, input().split())) for _ in range(m)]
    for a, b, d in c:
        adj[a].append((b, d))
        adj[b].append((a, -d))
    for i in range(1, n+1): dfs(i)
    f = 1
    for i in range(1, m+1):
        a, b, d = c[i-1]
        if val[a] + d != val[b]:
            print("NO")
            f = 0
            break
    if f: print("YES")

