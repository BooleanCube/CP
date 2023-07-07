import sys


t = int(input())
o = []
input = sys.stdin.readline
print = lambda x: sys.stdout.write(x + "\n")
for _ in range(t):
    n = int(input())
    r = []
    for _ in range(n):
        a, b = map(int, input().split())
        r.append((a-b))
    o.append(len([1 for c in r if c>0]))
print("\n".join(map(str,o)))
