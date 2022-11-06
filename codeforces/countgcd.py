t = int(input())
for z in range(t):
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    s = 1
    for i in range(1, n):
        if l[i-1]%l[i]: s=0; break
        a = l[i-1]//l[i]
        if a == 2: a = l[i-1]
        v = m-round(m/a)
        s *= v
        s %= 998244353
    print(s)
