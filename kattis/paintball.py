import math


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n

    def Find(self, x):
        s = x
        while self.par[s] >= 0:
            s = self.par[s]
        while x != s:
            t = self.par[x]
            self.par[x] = s
            x = t
        return s

    def Union(self, x, y):
        px = self.Find(x)
        py = self.Find(y)
        if px == py:
            return
        if self.par[px] > self.par[py]:
            px, py = py, px
        self.par[px] += self.par[py]
        self.par[py] = px


def dis(i, j):
    dx = p[i][0] - p[j][0]
    dy = p[i][1] - p[j][1]
    return math.sqrt(dx**2 + dy**2)


eps = 1e-8
N = 1002
p = [[0.0, 0.0] for _ in range(N)]
r = [0.0] * N


def cmp(x, y):
    if abs(x-y) <= eps:
        return 0
    return 1 if x-y > 0 else -1


n = int(input())
ufds = UnionFind(n+2)

for i in range(1, n + 1):
    x, y, rad = map(float, input().split())
    p[i] = [x, y]
    r[i] = rad

    if cmp(p[i][1] - r[i], 0) <= 0:
        ufds.Union(0, i)

    if cmp(p[i][1] + r[i], 1000) >= 0:
        ufds.Union(i, n + 1)

    for j in range(1, i):
        if cmp(dis(i, j), r[i] + r[j]) <= 0:
            ufds.Union(i, j)

if ufds.Find(0) == ufds.Find(n + 1):
    print("IMPOSSIBLE")
    exit(0)

ans1 = 1000.0
ans2 = 1000.0

for i in range(1, n + 1):
    if ufds.Find(i) != ufds.Find(n + 1):
        continue

    if cmp(p[i][0] - r[i], 0) <= 0:
        dx = p[i][0]
        dy = r[i]
        ans1 = min(ans1, p[i][1] - math.sqrt(dy**2 - dx**2))

    if cmp(p[i][0] + r[i], 1000) >= 0:
        dx = 1000 - p[i][0]
        dy = r[i]
        ans2 = min(ans2, p[i][1] - math.sqrt(dy**2 - dx**2))

print(f"0.00 {ans1:.2f} 1000.00 {ans2:.2f}")

