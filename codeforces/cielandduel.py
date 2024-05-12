from collections import defaultdict

n, m = map(int, input().split())
oc = defaultdict(list)
for _ in range(n):
    line = input().split()
    oc[line[0][0]].append(int(line[1]))
oc["A"].sort(); oc["D"].sort()

cnt, ans = 0, 0

mc = sorted([int(input()) for _ in range(m)], reverse=True)

"""
print(oc["A"])
print(mc[::-1])
print(mc)
a, b = [-oc["A"][i] + mc[::-1][i] for i in range(min(len(oc["A"]), len(mc)))], [-oc["A"][i] + mc[i] for i in range(min(len(oc["A"]), len(mc)))]
print(a, sum(a))
print(b, sum(b))
"""

for i in range(min(len(oc["A"]), m)):
    if mc[i] < oc["A"][i]: break
    ans += mc[i] - oc["A"][i]

mc.sort()

i, vis = 0, [0]*m
for d in oc["D"]:
    while i < m and mc[i] <= d: i += 1
    if i == m:
        print(ans)
        exit(0)
    mc[i], vis[i] = 0, 1
    i += 1

i = 0
for a in oc["A"]:
    while i < m and (mc[i] < a or vis[i]): i += 1
    if i == m:
        print(ans)
        exit(0)
    mc[i] -= a
    i += 1

ans = max(ans, sum(mc))
print(ans)
