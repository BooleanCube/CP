import math

n, s = map(int, input().split())
l = []
for _ in range(n):
    x, y, k = map(int, input().split())
    r = math.sqrt(x*x + y*y)
    l.append((r, 1e6-k))
l.sort()

s = 1000000-s
idx = -1
while s>0 and idx < len(l)-1:
    idx += 1
    s -= 1e6-l[idx][1]
print(l[idx][0] if s <= 0 else -1)

