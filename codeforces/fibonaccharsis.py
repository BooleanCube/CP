import math
import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x)+"\n")

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    f = 0
    ans = 0
    for i in range(math.ceil(n/2), n+1):
        w = 1
        a, b = i, n
        for j in range(k-2):
            b -= a
            a, b = b, a
            if a > b: w=0; break
        if not w and f:
            break
        elif w:
            f = 1
            ans += 1
    print(ans)
