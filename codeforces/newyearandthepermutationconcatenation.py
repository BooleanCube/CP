MOD = 998244353

def factorial(n, k):
    ans = 1
    for i in range(k+1, n+1):
        ans *= i
        ans %= MOD
    return ans

n = int(input())
if n == 1:
    print(1)
    exit(0)
ans = n * factorial(n, 0) - n
ans %= MOD

t = n
for k in range(n-1, 1, -1):
    t *= k
    t %= MOD
    ans -= t
    ans %= MOD

print(ans)