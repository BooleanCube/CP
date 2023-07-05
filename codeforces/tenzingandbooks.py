t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    l = [list(map(int, input().split()))[::-1] for _ in range(3)]
    ck = 0
    while 1:
        if ck == x:
            print("YES")
            break
        if len(l[0]) > 0 and x|l[0][-1]==x:
            ck|=l[0].pop(-1)
        elif len(l[1]) > 0 and x|l[1][-1]==x:
            ck|=l[1].pop(-1)
        elif len(l[2]) > 0 and x|l[2][-1]==x:
            ck|=l[2].pop(-1)
        else:
            print("NO")
            break
        if ck == x:
            print("YES")
            break
