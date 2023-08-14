n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
l = []
for row in grid:
    c = 0
    for col in row:
        if col == 1: c += 1
        elif c > 0: l.append(c); c = 0
    if c>0: l.append(c)
l.sort(reverse=True)
print(sum(l[:min(len(l), k)]))
