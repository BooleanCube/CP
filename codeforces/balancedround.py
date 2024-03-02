for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    ans, t = 0, 1
    l.sort()
    for i in range(1, n):
        if abs(l[i]-l[i-1]) <= k: t+=1
        else:
            ans = max(ans, t)
            t = 1
    ans = max(ans, t)
    print(n-ans)
