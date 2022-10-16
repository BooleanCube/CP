t = int(input())
for z in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = input()
    m = {}
    b = True
    for i in range(n):
        if l[i] in m and m[l[i]] != s[i]: b=False;break
        m[l[i]] = s[i]
    print("YES" if b else "NO")
