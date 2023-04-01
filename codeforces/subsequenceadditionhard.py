t = int(input())

for _ in range(t):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    ps = [0]*(n+1)
    for i in range(1, n+1):
        ps[i] = ps[i-1]+l[i-1]
    f = 1
    if l[0] > 1:
        print("no")
        continue
    for i in range(1, n):
        s = ps[i]-ps[0]
        x = l[i-1]
        r = i
        # print(i, l[i], s, x, r)
        if l[i] > s:
            f = 0
            break
    print("yes" if f else "no")
