t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans, idx = 0, n-1
    while idx > 0:
        if l[idx-1] > l[idx]:
            ans += l[idx-1]-l[idx]
            l[idx-1] = l[idx]
        idx -= 1
    print(ans)
