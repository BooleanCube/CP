from math import log2, ceil
# from fractions import Fraction
import sys

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

tc = int(input())
otpt = []

while tc:
    tc -= 1
    n = int(input())
    l = list(map(int, input().split()))
    nums = [log2(a) for a in l]
    ans = 0
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            p = ceil(nums[i-1]-nums[i]-(1e-9))
            ans += p
            nums[i] += p
    print(ans)