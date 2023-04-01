t = int(input())
for _ in range(t):
    n, m, x1, y1, x2, y2, d_string = input().split()
    n = int(n)
    m = int(m)
    x1 = int(x1)-1
    x2 = int(x2)-1
    y1 = int(y1)-1
    y2 = int(y2)-1
    d = (1 if d_string[0] == 'U' else 0) + (2 if d_string[1] == 'R' else 0)
    vis = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    i = x1
    j = y1
    bounces = 0
    flag = 1
    while not vis[i][j][d]:
        if i == x2 and j == y2:
            print(bounces)
            flag = 0
            break
        na = 0
        if d % 2 == 1 and i == 0:
            d -= 1
            na += 1
        if d % 2 == 0 and i == n - 1:
            d += 1
            na += 1
        if d >= 2 and j == m - 1:
            d -= 2
            na += 1
        if d < 2 and j == 0:
            d += 2
            na += 1
        bounces += min(1, na)
        if vis[i][j][d]:
            break
        vis[i][j][d] = True
        if d % 2 == 1:
            i -= 1
        else:
            i += 1
        if d >= 2:
            j += 1
        else:
            j -= 1
    if flag:
        print(-1)
