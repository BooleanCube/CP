import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

t = int(input())
o = []
for _ in range(t):
    n, w, h = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort()
    area, slope = w*h/2, h/(w/2)
    tot = area
    for i in range(len(trees)-1):
        space = trees[i+1]-trees[i]
        if space >= h:
            tot += area
        else:
            nh = trees[i]+h-trees[i+1]
            nw = w - (space/slope)*2
            tot += area - nw*nh/2
    o.append(tot)

print("\n".join(map(str,o)))
