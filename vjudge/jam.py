from math import hypot, atan2, acos, cos, sin

EPSILON = 1e-6

tc = int(input())

def inside(a, b):
    dc = hypot(b[0]-a[0], b[1]-a[1])
    if dc+EPSILON >= a[2]: return 0
    return dc + b[2] + EPSILON <= a[2]

def intersects(a, b):
    ans = []
    d = hypot(b[0]-a[0], b[1]-a[1])
    if d > a[2] + b[2] + EPSILON: return []
    if inside(a,b) or inside(b,a): return []
    cur_angle = atan2(b[1] - a[1], b[0] - a[0])
    if abs(d - a[2] - b[2]) <= EPSILON:
        pt = (a[0] + cos(cur_angle)*a[2], a[1] + sin(cur_angle)*a[2])
        ans.append(pt)
    else:
        angle = acos((b[2]**2 - a[2]**2 - d**2) / (-2 * a[2] * d))
        t1, t2 = cur_angle + angle, cur_angle - angle
        p1, p2 = (a[0] + cos(t1)*a[2], a[1] + sin(t1)*a[2]), (a[0] + cos(t2)*a[2], a[1] + sin(t2)*a[2])
        ans.append(p1)
        ans.append(p2)
    return ans

def solve():
    n = int(input())
    c = [tuple(map(int, input().split())) for _ in range(n)]
    pts = []
    for i in range(n):
        for j in range(n):
            if i == j: continue
            pts += intersects(c[i], c[j])
        d, r = hypot(c[i][0], c[i][1]), c[i][2]
        if d == 0:
            pts.append((r, 0))
            continue
        pts.append((c[i][0]/d * (d-r), c[i][1]/d * (d-r)))
    ans = 1e99
    for pt in pts:
        f = 1
        for j in c:
            d = hypot(pt[0]-j[0], pt[1]-j[1])
            if d + EPSILON < j[2]: f = 0
        if f: ans = min(ans, hypot(*pt))
    print("%.3f" % ans)

while tc:
    solve()
    tc -= 1
