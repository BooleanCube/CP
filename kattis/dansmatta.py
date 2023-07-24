from collections import defaultdict
import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x)+"\n")

n = int(input())
steps = ["".join(sorted(input())).strip() for _ in range(n)]
dirs = "HNUV"
dp = [[defaultdict(lambda: 10**6) for _ in range(4)] for _ in range(n+1)]
dp[0][0][3] = dp[0][3][0] = 0

for i in range(n):
    step = steps[i]
    if len(step) == 1:
        l = dirs.find(step)
        for lp in range(4):
            for rp in range(4):
                if lp==rp: continue
                if l!=rp: dp[i+1][l][rp] = min(dp[i+1][l][rp], dp[i][lp][rp]+int(l!=lp))
                if l!=lp: dp[i+1][lp][l] = min(dp[i+1][lp][l], dp[i][lp][rp]+int(l!=rp))
        continue
    l, r = map(lambda x: dirs.find(x), step)
    for lp in range(4):
        for rp in range(4):
            if lp==rp: continue
            dp[i+1][l][r] = min(dp[i+1][l][r], dp[i][lp][rp]+int(l!=lp)+int(r!=rp))
            dp[i+1][r][l] = min(dp[i+1][r][l], dp[i][lp][rp]+int(r!=lp)+int(l!=rp))

print(min(dp[-1][lp][rp] for lp in range(4) for rp in range(4)))
