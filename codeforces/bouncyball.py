import sys
input = sys.stdin.readline
print = lambda l: sys.stdout.write(l)

t = int(input())
out = ""
for _ in range(t):
    h,w,si,sj,ei,ej,sd = input().split()
    h=int(h);w=int(w);si=int(si);sj=int(sj);ei=int(ei);ej=int(ej)
    v = set()
    current = (si, sj, sd)
    bounces = 0
    flag = 1
    while current not in v:
        v.add(current)
        d = current[2]
        if d=="DR":
            if ej-current[1] == ei-current[0] and ei-current[0]>=0:
                flag = 0
                break
            dist = min(w-current[1], h-current[0])
            current = (current[0]+dist, current[1]+dist)
            bounces += 1
            if current[1] == w and current[0] == h:
                d = "UL"
            elif current[1] == w:
                d = "DL"
            elif current[0] == h:
                d = "UR"
        elif d=="DL":
            if current[1]-ej == ei-current[0] and ei-current[0]>=0:
                flag = 0
                break
            dist = min(current[1]-1, h-current[0])
            current = (current[0]+dist, current[1]-dist)
            bounces += 1
            if current[1] == 1 and current[0] == h:
                d = "UR"
            elif current[1] == 1:
                d = "DR"
            elif current[0] == h:
                d = "UL"
        elif d=="UR":
            if ej-current[1] == current[0]-ei and current[0]-ei>=0:
                flag = 0
                break
            dist = min(w-current[1], current[0]-1)
            current = (current[0]-dist, current[1]+dist)
            bounces += 1
            if current[0] == 1 and current[1] == w:
                d = "DL"
            elif current[0] == 1:
                d = "DR"
            elif current[1] == w:
                d = "UL"
        elif d=="UL":
            if current[1]-ej == current[0]-ei and current[0]-ei>=0:
                flag = 0
                break
            dist = min(current[1]-1, current[0]-1)
            current = (current[0]-dist, current[1]-dist)
            bounces += 1
            if current[0] == 1 and current[0] == 1:
                d = "DR"
            elif current[0] == 1:
                d = "DL"
            elif current[1] == 1:
                d = "UR"
        current = (current[0], current[1], d)
    out += str(bounces)+"\n" if not flag else "-1\n"

            
print(out)
