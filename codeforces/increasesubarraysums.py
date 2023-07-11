def f(l, n, x):
    ans = []
    mx = [-1e9]*(n+1)
    for lp in range(n):
        s = 0
        for rp in range(lp, n):
            s += l[rp]
            mx[rp-lp+1] = max(mx[rp-lp+1], s)
    for k in range(n+1):
        s = 0
        for i in range(1, n+1):
            s = max(s, mx[i] + min(i,k)*x)
        ans.append(s)
    return ans



tc = int(input())
for _ in range(tc):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    print(*f(l, n, x))
