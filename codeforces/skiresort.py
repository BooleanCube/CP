t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    l = list(map(int, input().split()))
    c = 0
    ans = 0
    for i in range(n):
        if l[i] <= q:
            c += 1
        else:
            ans += sum(c-j+1 for j in range(k, c+1))
            c = 0
    if c > 0:
        ans += sum(c-j+1 for j in range(k, c+1))
    print(ans)
