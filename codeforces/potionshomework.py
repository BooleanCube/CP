MOD = 10**4+7

n = int(input())
l = sorted([int(input()) for _ in range(n)])
s = 0
for i in range(n):
    s += l[i]*l[-i-1]
    s %= MOD
print(s)
