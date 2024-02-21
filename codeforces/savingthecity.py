import sys

input = sys.stdin.readline
print = lambda *args : sys.stdout.write(" ".join(map(str, args)) + "\n")

tc = int(input())

while tc:
	tc -= 1
	a, b = map(int, input().split())
	city = input()
	if "1" not in city:
		print(0)
		continue
	city = city[city.find("1"):city.rfind("1")+1]
	l = []
	cl = 0
	for i in range(len(city)):
		if city[i] == "1":
			if cl: l.append(cl)
			cl = 0
		elif city[i-1] == "0": cl += 1
		else: cl = 1
	l.sort(reverse=True)
	tans = a*(len(l)+1)
	ans = tans
	for i in range(len(l)):
		g = l.pop(-1)
		tans += g*b - a
		ans = min(ans, tans)
	print(ans)
