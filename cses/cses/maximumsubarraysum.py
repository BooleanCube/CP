n = int(input())
ps = [0] + list(map(int, input().split()))
for i in range(1, n): ps[i+1] += ps[i]
m = -1e10
lp, rp = 1, 1
while lp <= rp <= n:
    s = ps[rp] - ps[lp-1]
    m = max(m, s)
    if lp == rp: rp += 1
    elif s < 0: lp = rp
    elif ps[rp]-ps[lp] > s: lp += 1
    else: rp += 1
print(m)
