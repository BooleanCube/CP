

tc = int(input())

while tc:
    tc -= 1
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    b = [a%k if a%k else k for a in l]
    ans = min([k-a for a in b])
    if k == 4:
        cnt0 = 0
        for a in l:
            if a&1 == 0: cnt0 += 1
        ans = min(ans, (0 if cnt0 >= 2 else 1 if cnt0 >= 1 else 2))
    print(ans)