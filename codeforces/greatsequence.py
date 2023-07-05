from collections import Counter

tc = int(input())
for _ in range(tc):
    n, x = map(int, input().split())
    l = sorted(map(int, input().split()))
    m = Counter(l)
    idx = ans = 0
    while idx < n:
        if m[l[idx]] == 0:
            idx += 1
            continue
        if l[idx]*x in m and m[l[idx]*x] > 0:
            m[l[idx]*x] -= 1
            m[l[idx]] -= 1
        else:
            m[l[idx]] -= 1
            ans += 1
        idx += 1
    print(ans)
