from collections import Counter

tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())
    s = input()
    fq = Counter(s)
    cnt = sum(1 for c in set(s) if fq[c] & 1)
    if cnt > k+1: print("NO")
    else: print("YES")