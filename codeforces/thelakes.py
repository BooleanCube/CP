def dfs(grid, i, j):
    stack = [(i, j)]
    volume = 0
    while stack:
        x, y = stack.pop()
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            continue
        volume += grid[x][y]
        grid[x][y] = 0
        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))
    return volume

def lv(grid):
    mv = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:
                mv = max(mv, dfs(grid, i, j))
    return mv

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    print(lv(grid))
