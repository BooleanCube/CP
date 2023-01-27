t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input()))
    ps = [0, a[0]]
    for i in range(1,n): ps.append(ps[i]+a[i])
    cnt = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            v = ps[j]-ps[i-1]
            if v == j-i+1: cnt += 1
    print(cnt)
