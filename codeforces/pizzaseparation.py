n = int(input())
l = sorted(map(int, input().split()))
mn = 1e99
i, lp = 0, 0
for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += l[j]
        mn = min(mn, 2*abs(180-sm))
print(mn)
