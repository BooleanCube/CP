tc = int(input())

while tc:
    tc -= 1
    n, k = map(int, input().split())
    start = (0, 0)
    graph = [input() for _ in range(3)]
    for i in range(3):
        for j in range(n):
            if graph[i][j] == "s": start = (i, j)
    stack = []; stack.append(start)
    vis = set()
    adj = [-1, 0, 1]
    f = 0
    while stack:
        cur = stack.pop(-1)
        if cur in vis: continue
        vis.add(cur)
        x, y = cur
        if y >= n-1:
            f = 1
            break
        if graph[x][y+1] != ".":
            continue
        for k in range(3):
            i, j = x+adj[k], y+3
            if not (0<=i<3): continue
            if (i, j) in vis: continue
            if graph[i][y+1] != ".": continue
            if j < n and graph[i][j] != ".": continue
            stack.append((i, j))
    if f: print("YES")
    else: print("NO")