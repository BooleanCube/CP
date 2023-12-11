from collections import defaultdict
s = list(map(int, list(input())))
n = len(s)
ps = []; ps.append(tuple([0]*10))
for i in range(n):
    cs = list(ps[i])
    cs[s[i]] += 1
    cs[s[i]] &= 1
    ps.append(tuple(cs))
fq = defaultdict(int)
ans = 0
for i in range(n+1):
    ans += fq[ps[i]]
    fq[ps[i]] += 1
print(ans)
