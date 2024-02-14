from collections import defaultdict

def fastexpo(b, e, m):
    if e <= 1: return b
    if e & 1: return (b * fastexpo(b, e-1, m)) % m
    v = fastexpo(b, e>>1, m)
    return (v * v) % m

s = input(); n = len(s)
suffix = [0]*(n+1)
sufstrl = 0
for i in range(n-1, -1, -1):
    sufstrl += 1
    suffix[i] = ((int(s[i])*fastexpo(10, sufstrl, 2019)) % 2019 + suffix[i+1]) % 2019
fq = defaultdict(int)
ans = 0
for i in range(n+1):
    ans += fq[suffix[i]]
    fq[suffix[i]] += 1
print(ans)