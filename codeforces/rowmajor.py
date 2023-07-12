import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x)+"\n")

tc = int(input())
for _ in range(tc):
    n = int(input())
    f = set([i for i in range(2,min(n,26*2)) if n%i == 0])
    a = "abcdefghijklmnopqrstuvwxyz"
    if 26 in f:
        for c in a:
            if 26+ord(c)-97 in f or 26-ord(c)-97 in f:
                continue
            else:
                a += c
                break
    print((a*100000)[:n])

