from math import gcd
from collections import Counter

MN = int(1e5+1)
n = int(input())
l = list(map(int, input().split()))
fq = Counter(l)
ans = 1

for i in range(2, MN):
    cur = 0
    for j in range(i, MN, i):
        cur += fq[j]
    ans = max(ans, cur)

print(ans)