from re import L


t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    l = list(map(int, input().split()))
    ans = tem =0
    for i in range(1, n):
        if abs(l[i]-l[i-1]) <= k: tem+=1
        else:
            ans = max(ans, tem)
            tem = 1
    l.sort()
    tem = 1
    for i in range(1, n):
        if abs(l[i]-l[i-1]) <= k: tem+=1
        else:
            ans = max(ans, tem)
            tem = 1
    ans = max(ans, tem)
    print(n-ans)
