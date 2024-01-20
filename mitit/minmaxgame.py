from statistics import median
import math

n = int(input())
l = list(map(int, input().split()))
l.sort()

print(l[n//2])
