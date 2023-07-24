n, a, b = map(int, input().split())
ps = [0] + list(map(int, input().split()))
for i in range(1, n): ps[i+1] += ps[i]
m = -1e15
lp, rp = 1, 1
while lp <= rp <= n:
    s, l = ps[rp] - ps[lp-1], rp-lp+1
    print(lp, rp, s, l)
    if a <= l <= b: m = max(m, s)
    if l < a: rp += a-l
    elif l > b: lp += l-b
    elif lp == rp: rp += 1
    elif s < 0: lp = rp
    elif ps[rp]-ps[lp] > s: lp += 1
    else: rp += 1
print(m)

