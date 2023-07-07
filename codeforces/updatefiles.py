t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    n -= 1
    cur = 0
    ans = 0
    while n > 0:
        if 2**cur <= k:
            n -= 2**cur
            cur += 1
            ans += 1
        else:
            ans += n//k
            if n%k: ans += 1
            break
    print(ans)
