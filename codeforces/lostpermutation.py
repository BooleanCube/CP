n = int(input())
for i in range(n):
    m,s = map(int, input().split())
    l = list(map(int, input().split()))
    b = max(l)
    r = (b*(b+1)//2) - sum(l)
    if s<r: print("NO");continue
    while True:
        if r == s: print("YES");break
        if r>s: print("NO");break
        r += b+1
        b += 1

