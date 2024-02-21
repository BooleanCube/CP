import sys

input = sys.stdin.readline
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")

n, m = map(int, input().split())
v = set()
for _ in range(m):
	x, y = map(int, input().split())
	v.add(x-1); v.add(y-1)
k = -1
for i in range(n):
	if i not in v:
		k = i+1
		break
print(n-1)
for i in range(1, n+1):
	if i != k:
		print(k, i)
