import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if math.log2(n) < k:
        print(n+1)
    else:
        print(int(pow(2,k)))
    
