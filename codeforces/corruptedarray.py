t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(map(int, input().split()))
    p = sum(l[:-2])
    t = p + l[-2]
    if l[-1] > t:
        print(*l[:n] if p == l[-2] else -1)
    else:
        if not t-l[-1] in set(l):
            print(-1)
        else:
            l.remove(t-l[-1])
            print(*l[:-1])
