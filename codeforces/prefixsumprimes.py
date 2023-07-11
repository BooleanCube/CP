p = [1]*1000000
p[0] = p[1] = 0
for i in range(2, 1000000):
    for j in range(i+i, 1000000-i, i):
        p[j] = 0

primes = [i for i in range(len(p)) if p[i]]


n = int(input())
ts = list(map(int, input().split())).count(2)
os = n-ts
cur = 0
idx = 0
ans = []
while os > 0 or ts > 0:
    if primes[idx]-cur > 1:
        if ts > 0:
            ans.append(2)
            cur += 2
            ts -= 1
        else:
            ans.append(1)
            cur += 1
            os -= 1
    else:
        if os > 0:
            ans.append(1)
            cur += 1
            os -= 1
        else:
            ans.append(2)
            cur += 1
            ts -= 1
    while cur >= primes[idx]: idx += 1

print(*ans)
