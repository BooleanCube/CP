tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            cell = grid[i][j]
            if cell == "*":
                y = i
                while y<n-1 and grid[y+1][j] == ".":
                    grid[y][j] = "."
                    grid[y+1][j] = cell
                    y += 1
    for row in grid:
        print("".join(row))
