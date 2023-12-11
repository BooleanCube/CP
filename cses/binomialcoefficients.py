from math import comb
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(comb(a,b)%int(1e9+7))
