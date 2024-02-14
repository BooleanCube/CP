from math import isqrt, sqrt

tc = int(input())
while tc:
    tc -=1
    n = int(input())
    l = list(map(int, input().split()))
    print("YES" if isqrt(sum(l)) == sqrt(sum(l)) else "NO")