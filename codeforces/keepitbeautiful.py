t = int(input())
pr = []
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    f = 1
    p = -1
    o = []
    for i in range(n):
        x = l[i]
        if not f and p <= x <= l[0]:
            o.append("1")
            p = x
        elif f and x >= p:
            o.append("1")
            p = x
        elif f and x <= l[0]:
            f = 0
            o.append("1")
            p = x
        else:
            o.append("0")
    pr.append("".join(o))
print("\n".join(pr))
