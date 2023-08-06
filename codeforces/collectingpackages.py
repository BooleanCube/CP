t = int(input())
for _ in range(t):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    l.sort()
    cx, cy = 0, 0
    ans = ""
    f = 0
    for p in l:
        x, y = p[0], p[1]
        if x > cx:
            ans += "R"*(x-cx)
            cx = x
        if y < cy:
            print("NO")
            f = 1
            break
        else:
            ans += "U"*(y-cy)
            cy = y
    if f: continue
    print("YES")
    print(ans)
