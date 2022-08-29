import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
map = {}
b=0;l=1;k=0
for r in range(1,n+1):
    k = li[r-1]
    if k in map:
        b = max(b, r-l)
        l = max(l, map[k]+1)
        map[k] = r
    else:
        b = max(b, r-l+1)
        map[k] = r
print(b)
