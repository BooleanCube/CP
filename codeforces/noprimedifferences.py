p = [1]*1000005
p[0] = p[1] = 0
for i in range(2, len(p)):
    for j in range(i*2, len(p), i):
        p[j] = 0

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(range(m*i+1, m*i+m+1)))
    if p[m]:
        for i in range(n):
            if i&1 and i<n-1: grid[i], grid[i+1] = grid[i+1], grid[i]
            elif i<n-2: grid[i], grid[i+2] = grid[i+2], grid[i]
    if n == 4:
        grid[-1], grid[-2] = grid[-2], grid[-1]
    print("\n".join([" ".join(map(str, row)) for row in grid]))

