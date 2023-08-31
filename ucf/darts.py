import math

w, b,d,s = map(int, input().split())
darts = [tuple(map(float, input().split())) for _ in range(int(input()))]
n = len(darts)
sec = 360/w
ans = 0
for i in range(n):
    x,y = darts[i][0], darts[i][1]
    angle, rad = 0, 0
    if x==0: angle=90 if y>0 else 270; rad=abs(y)
    else:
        angle = math.degrees(math.atan(y/x))
        angle = angle+360 if angle<0 else angle
        if x<0 and y<=0: angle += 180
        if x<0 and y>0: angle -= 180
        rad = (x**2+y**2)**0.5
    if rad > s: continue
    elif rad > d: ans += angle//sec+1
    elif rad > b: ans += 2*(angle//sec+1)
    else: ans += 50
print(round(ans))
