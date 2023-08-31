from collections import deque

n = int(input())
lines = list(map(int, input().split()))
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())

q = deque()
q.append((sx, sy, 0))
v = set()
while len(q)>0:
    cx, cy, path = q.popleft()
    if (cx, cy) in v: continue
    v.add((cx, cy))
    if (cy,cx)==(ey,ex): print(path); exit(0)
    if cx==0 and cy>1: q.append((lines[cy-2], cy-1, path+1))
    elif cx>0: q.append((cx-1, cy, path+1))
    if cx==lines[cy-1] and cy<n: q.append((0, cy+1, path+1))
    elif cx<lines[cy-1]: q.append((cx+1, cy, path+1))
    if cy>1: q.append((min(cx, lines[cy-2]), cy-1, path+1))
    if cy<n: q.append((min(cx, lines[cy]), cy+1, path+1))
print("it should never get here lol")
