t = int(input())
for _ in range(t):
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    ans = 0
    if bx >= cx >= ax or cx >= bx >= ax:
        ans += min(bx,cx)-ax
    if ax >= bx >= cx or ax >= cx >= bx:
        ans += ax-max(bx,cx)
    if by >= cy >= ay or cy >= by >= ay:
        ans += min(by,cy)-ay
    if ay >= by >= cy or ay >= cy >= by:
        ans += ay-max(by,cy)
    print(ans + 1)
