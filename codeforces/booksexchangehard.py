from collections import defaultdict
import sys

input = sys.stdin.readline
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")

tc = int(input())

while tc:
	tc -= 1
	n = int(input())
	p = [0]+list(map(int, input().split()))
	clen = defaultdict(int)
	
	def dfs(start):
		if start in clen: return
		vis = set()
		cur = start
		while 1:
			if cur in vis:
				for elem in vis:
					clen[elem] = len(vis)
				return
			vis.add(cur)
			cur = p[cur]
	
	for i in range(1, n+1): dfs(i)
	print(*[clen[i] for i in range(1, n+1)])
