from random import *

n = int(input())

parent = [i for i in range(0, n+1)]
edges = []
for i in range(1, n+1):
    end, weight = map(int, input().split())
    edges.append((weight, i, end))
edges.sort(reverse=True)

def find(node):
    if parent[node] == node:
        return node
    return find(parent[node])

def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)
    if random()>0.5:
        parent[node1] = node2
    else:
        parent[node2] = node1

ans = 0

for edge in edges:
    w,s,e = edge[0], edge[1], edge[2]
    if find(s) != find(e):
        ans += w
        union(s, e)

print(ans)