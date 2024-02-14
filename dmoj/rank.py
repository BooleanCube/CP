from collections import defaultdict

graph = defaultdict(list)
n, k = map(int, input().split())
for _ in range(k):
    a, b, sa, sb = map(int, input().split())
    if sa > sb: a, b = b, a
    graph[a].append(b)

cycle = set()

def dfs(start):
    global cycle
    fro = [0]*(n+1)
    stack = [start]
    vis = set()
    f = 0
    while stack:
        cur = stack.pop(-1)
        # print(cur)
        if cur == start and f:
            # print("bruh", fro)
            curr = fro[cur]
            while curr != cur:
                # print(curr)
                cycle.add(curr)
                curr = fro[curr]
            cycle.add(cur)
            return
        if cur in vis: continue
        vis.add(cur)
        f = 1
        for nbr in graph[cur]:
            if nbr in vis and nbr != start: continue
            fro[nbr] = cur
            stack.append(nbr)

for i in range(1, n+1): dfs(i)
print(len(cycle))