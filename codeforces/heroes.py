from itertools import permutations
# from collections import defaultdict
import sys

input = sys.stdin.readline
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")

like = [[0]*7 for _ in range(7)]
tt = {}
co = 0

n = int(input())
for _ in range(n):
	s1, _, s2 = input().split()
	if s1 not in tt:
		tt[s1] = co
		co += 1
	if s2 not in tt:
		tt[s2] = co
		co += 1
	like[tt[s1]][tt[s2]] = 1

expe = list(map(int, input().split()))

diffb = 1e99
likb = 0

for arr in permutations(list(range(7))):
	# arr = list(arr)
	tot = [[0]*7 for _ in range(7)]

	for i in range(7):
		for j in range(i+1, 7):
			for x in range(i, j+1):
				for y in range(i, j+1):
					if like[arr[x]][arr[y]]:
						tot[i][j] += 1

	for i in range(5):
		xx = expe[0]//(i+1)
		lik = tot[0][i]
		for j in range(i+1, 6):
			yy = expe[1]//(j-i)
			lik += tot[i+1][j]
			zz = expe[2]//(6-j)
			lik += tot[j+1][6]
			diff = abs(xx - yy)
			diff = max(diff, abs(xx - zz))
			diff = max(diff, abs(yy - zz))
			if diff < diffb:
				diffb = diff
				likb = lik
			elif diff == diffb: likb = max(likb, lik)
			lik -= tot[i+1][j]
			lik -= tot[j+1][6]

print(diffb, likb)
