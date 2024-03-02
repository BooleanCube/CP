from collections import Counter, OrderedDict

for _ in range(int(input())):
    n = int(input())
    l = [e for e in list(map(int, input().split())) if e <= n]
    fq, cnt = OrderedDict(Counter(l)), OrderedDict()
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if j not in cnt: cnt[j] = 0
            cnt[j] += fq[i] if i in fq else 0
            ans = max(ans, cnt[j])
    print(ans)
