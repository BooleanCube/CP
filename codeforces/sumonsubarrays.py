tc = int(input())
for _ in range(tc):
    n, k = map(int, input().split())
    l = list(range(5, n+5))
    ps = [0]*(n+1)
    for i in range(1, n+1):
        ps[i] += ps[i-1] + l[i-1]
    t = n*(n+1)//2 - k
    idx = n-1
    while t > idx+1:
        s = ps[idx] - ps[0]
        l[idx] = -(s+1)
        t -= idx+1
        idx -= 1
    l[idx] = -(ps[idx] - ps[idx-t+1] + 1)
    print(*l)
