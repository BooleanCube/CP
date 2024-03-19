from collections import Counter

def eq(a, b):
    for k in a:
        if a[k] and a[k] != b[k]: return 0
    for k in b:
        if b[k] and b[k] != a[k]: return 0
    return 1

def solve():
    n = int(input())
    s = input()
    if (n+1) & 1:
        print(0)
        return
    m = n >> 1
    fh, sh = Counter(s[:m+1]), Counter(s[m:])
    ans = 0
    for i in range(n):
        fh[s[m]] -= 1
        sh[s[m]] -= 1
        if i < m:
            fh[s[m]] += 1
            fh[s[i]] -= 1
        if i > m:
            sh[s[m]] += 1
            sh[s[i]] -= 1
        if eq(fh, sh): ans += 1
        fh[s[m]] += 1
        sh[s[m]] += 1
        if i < m:
            fh[s[m]] -= 1
            fh[s[i]] += 1
        if i > m:
            sh[s[m]] -= 1
            sh[s[i]] += 1
    print(ans)

tc = int(input())
while tc:
    solve()
    tc -= 1
