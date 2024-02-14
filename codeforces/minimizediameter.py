from collections import deque
import sys

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

def bfs(tree, start):
    q = deque(); q.append((start, 1))
    vis = [0]*len(tree)
    last = 0
    while q:
        cur, path = q.popleft()
        if vis[cur-1]: continue
        last = (cur, path)
        vis[cur-1] = 1
        for nbr in tree[cur]:
            if vis[nbr-1]: continue
            q.append((nbr, path+1))
    return last

n = int(input())
a = [0]*(n+1)
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    if a[n1] == 0: a[n1] = []
    if a[n2] == 0: a[n2] = []
    a[n1].append(n2)
    a[n2].append(n1)
m = int(input())
b = [0]*(m+1)
for _ in range(m-1):
    n1, n2 = map(int, input().split())
    if b[n1] == 0: b[n1] = []
    if b[n2] == 0: b[n2] = []
    b[n1].append(n2)
    b[n2].append(n1)

aenp = bfs(a, 1)
ad = bfs(a, aenp[0])[1]
benp = bfs(b, 1)
bd = bfs(b, benp[0])[1]

print(max(ad-1, bd-1, ((ad+2)>>1) + (((bd+2)>>1)) - 1))
