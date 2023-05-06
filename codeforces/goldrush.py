dp = {}
for i in range(3, 10000000, 3):
    a = i//3
    b = 2*a
    dp[i] = {a,b}
    dp[i].update(dp.get(a, set()))
    dp[i].update(dp.get(b, set()))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print("yes" if n==m or (n%3 == 0 and m in dp[n]) else "no")
