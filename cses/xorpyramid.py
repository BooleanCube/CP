from collections import defaultdict

n = int(input())
l = list(map(int, input().split()))
mp = defaultdict(int)
for i in range(len(l)):
    b = bin(l[i])[2:]
    if i == 0 or i == n-1:
        m = len(b)
        for i in range(m-1, -1, -1):
            mp[m-i] += int(b[i])
    else:
        m = len(b)
        for i in range(m-1, -1, -1):
            mp[m-i] += int(b[i])*2
print(int("".join([str(mp[c]&1) for c in sorted(mp.keys())[::-1]]), 2))
