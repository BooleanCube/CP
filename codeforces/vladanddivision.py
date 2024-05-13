from collections import Counter
import sys

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

tc = int(input())

while tc:
    tc -= 1
    n = int(input())
    l = list(map(int, input().split()))
    fq = Counter(l)
    cnt = 0
    for i in l:
        if fq[i] <= 0: continue
        fq[i] -= 1
        if fq[i ^ ((1 << 31)-1)]:
            fq[i ^ ((1 << 31)-1)] -= 1
            cnt += 1
    print(len(l)-cnt)
