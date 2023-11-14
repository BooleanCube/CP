from math import atan2
import math

EPS = 1e-6
PI = math.pi

def area(pts):
    res = 0
    for i in range(len(pts)):
        n = len(pts)
        res += (pts[i][0]*pts[(i+1)%n][1]) - (pts[i][1]*pts[(i+1)%n][0])
    return abs(res)/2

def inpolygon(pt, pts):
    if len(pts) == 0: return
    s = 0
    for i in range(len(pts)):
        if ccw(pts[i], pt, pts[(i+1)%n]): s += angle(pts[i], pt, pts[(i+1)%n])
        else: s -= angle(pts[i], pt, pts[(i+1)%n])
    return abs(abs(s-2*PI)) < EPS

def cmpangle(p1, p2):
    return atan2(y,x)

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    line = input().split()
    ptsa, ptsb = [], []
    for i in range(0, n*2, 2):
        ptsa.append((int(line[i]), int(line[i+1])))
    line = input().split()
    for i in range(0, m*2, 2):
        ptsb.append((int(line[i]), int(line[i+1])))
    pts = ptsa + ptsb
    for i in range(len(ptsa)):
        for j in range(len(ptsb)):
            fpa, spa = ptsa[i], ptsa[(i+1)%n]
            fpb, spb = ptsb[j], ptsb[(j+1)%m]
            la, lb, xcrd, ycrd = (0, 0), (0, 0), 0, 0
            ma, mb = 32457, 3456
            if (spa[0]-fpa[0]) != 0:
                ma = (spa[1]-fpa[1])/(spa[0]-fpa[0])
                la = (ma, fpa[1]-ma*fpa[0]) #(slope, yint)
            else:
                la = (fpa[0],)
            if (spb[0]-fpb[0]) != 0:
                mb = (spb[1]-fpb[1])/(spb[0]-fpb[0])
                lb = (mb, fpb[1]-mb*fpb[0]) #(slope, yint)
            else:
                lb = (fpb[0],)
            if len(la) == 1:
                if len(lb) == 1: continue
                xcrd = la[0]
                ycrd = mb*xcrd + lb[1]
            elif len(lb) == 1:
                xcrd = lb[0]
                ycrd = ma*xcrd + la[1]
            else:
                if ma == mb: continue
                xcrd = (lb[1]-la[1])/(la[0]-lb[0])
                ycrd = la[0]*xcrd + la[1]
            x1, x2, y1, y2 = min(fpa[0], spa[0]), max(fpa[0], spa[0]), min(fpa[1], spa[1]), max(fpa[1], spa[1])
            xb1, xb2, yb1, yb2 = min(fpb[0], spb[0]), max(fpb[0], spb[0]), min(fpb[1], spb[1]), max(fpb[1], spb[1])
            if x1 <= xcrd <= x2 and y1 <= ycrd <= y2 and xb1 <= xcrd <= xb2 and yb1 <= ycrd <= yb2:
                pts.append((xcrd, ycrd))
    print(pts)