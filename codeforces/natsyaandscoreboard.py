digs = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]

n, k = map(int, input().split())
dist = [[0]*10 for _ in range(n)]
s = [input() for _ in range(n)]
for i in range(n):
    for d in range(10):
        for j in range(7):
            if s[i][j] == '1' and digs[d][j] == '0':
                dist[i][d] = -1
                break
            if s[i][j] == '0' and digs[d][j] == '1': dist[i][d] += 1

dp = [[0]*(k+1) for _ in range(n+1)]
dp[n][0] = 1
for i in range(n, 0, -1):
    for j in range(k+1):
        if dp[i][j]:
            for d in range(10):
                if dist[i-1][d] != -1 and j + dist[i-1][d] <= k:
                    dp[i-1][j+dist[i-1][d]] = 1

if dp[0][k] == 0:
    print(-1)
    exit(0)

ans = ""
for i in range(n):
    cur = "-1"
    for d in range(9, -1, -1):
        if dist[i][d] != -1 and k >= dist[i][d] and dp[i+1][k-dist[i][d]]:
            cur = str(d)
            k -= dist[i][d]
            break
    ans += cur

print(ans)
