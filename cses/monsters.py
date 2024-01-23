from collections import deque


adj = [1, -1, 0, 0]
dirs = "DULR"

n, m = map(int, input().split())
grid = []
start = (0, 0)
for i in range(n):
    grid.append(input())
    for j in range(m):
        if grid[i][j] == "A": start = (i, j)

q, vis = deque(), set()
q.append((start, ""))
while len(q):
    cur, path = q.popleft()
    if cur in vis: continue
    x, y = cur
    if x == n-1 or x == 0 or y == m-1 or y == 0:
        print("YES")
        print(len(path))
        print(path)
        exit(0)
    vis.add(cur)
    for k in range(4):
        dx, dy = adj[k], adj[-k-1]
        dd = dirs[k]
        nloc = (x+dx, y+dy)
        if nloc in vis: continue
        if grid[x+dx][y+dy] != ".": continue
        q.append((nloc, path+dd))

print("NO")
