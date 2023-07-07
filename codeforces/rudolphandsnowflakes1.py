import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

p = set()
for k in range(2, 10**6+1):
    s = 1 + k + k**2
    po = 3
    while s <= 10**6:
        p.add(s)
        s += k**po
        po += 1

t = int(input())
o = []
for _ in range(t):
    n = int(input())
    o.append("YES" if n in p else "NO")

print("\n".join(o))
