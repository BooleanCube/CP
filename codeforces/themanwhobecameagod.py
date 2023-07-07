def calculate_min_power(n, k, suspicions):
    dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for l in range(j):
                dp[i][j] = min(dp[i][j], dp[i - 1][l] + abs(suspicions[j - 1] - suspicions[l]))

    return dp[k][n-1]

def solve(t, test_cases):
    for _ in range(t):
        n, k, suspicions = test_cases[_]
        min_power = calculate_min_power(n, k, suspicions)
        print(min_power)

t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    suspicions = list(map(int, input().split()))
    test_cases.append((n, k, suspicions))

solve(t, test_cases)

