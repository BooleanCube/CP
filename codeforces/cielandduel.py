from collections import defaultdict

n, m = map(int, input().split())
oc = defaultdict(list)
for _ in range(n):
    line = input().split()
    oc[line[0][0]].append(int(line[1]))
oc["A"].sort(); oc["D"].sort(reverse=1)
mc = sorted([int(input()) for _ in range(m)])

cnt, ans = 0, 0
for i in range(min(len(oc["A"]), m)):
    v = -1
    for j in range(len(mc)-1, -1, -1):
        if mc[j] >= oc["A"][i]: v = mc[j]
        else: break
    if v > -1: mc.remove(v)
    if v >= oc["A"][i]:
        cnt += 1
        ans += v - oc["A"][i]
    else: break

if cnt == len(oc["A"]):
    for i in range(min(len(mc), len(oc["D"]))):
        v = -1
        for j in range(len(mc)-1, -1, -1):
            if mc[j] > oc["D"][i]: v = mc[j]
            else: break
        if v > -1: mc.remove(v)
        if v > oc["D"][i]: cnt += 1
        else: break

if cnt == n: ans += sum(mc)

print(ans)