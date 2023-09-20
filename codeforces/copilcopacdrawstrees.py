from collections import defaultdict

nmax = 3*10**5+5
inf = 10**9

n = 0
vis = [0]*nmax
d = [0]*nmax
mp = defaultdict(list)

def dfs(node, t):
    stack = [(node, t)]
    vis[node] = 1

    while stack:
        node, t = stack.pop()

        for u, c in mp[node]:
            if not vis[u]:
                d[u] = (c<t)+d[node]
                stack.append((u, c))
                vis[u] = 1

tc = int(input())

while tc > 0:
    tc -= 1
    n = int(input())

    for i in range(1, n):
        u, v = map(int, input().split())

        mp[u].append((v, i))
        mp[v].append((u, i))

    for i in range(1, n+1):
        vis[i] = 0

    d[1] = 0
    dfs(1, n)

    m = 0

    for i in range(1, n+1):
        m = max(m, d[i])

    print(m)

    for i in range(1, n+1):
        mp[i].clear()

