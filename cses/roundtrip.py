import sys

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

n, m = map(int, input().split())
graph = [[]]*(n+1)
print(graph)
for _ in range(m):
    a, b = map(int, input().split())
    if graph[a] == 0: graph[a] = []
    if graph[a] == 0: graph[a] = []
