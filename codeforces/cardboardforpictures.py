for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    l, r, m = 0, 10**9, 0
    while l <= r:
        m = l + ((r-l)>>1)
        s = sum((a[i]+2*m)**2 for i in range(n))
        if s == c: break
        elif s > c: r = m-1
        else: l = m+1
    print(m)
