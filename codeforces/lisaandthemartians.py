tc = int(input())

while tc:
    tc -= 1
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = [(l[i], i+1) for i in range(n)]
    l.sort()
    ans, ai, bi, xi = -1, 0, 0, 0
    for i in range(1, n):
        a, aidx = l[i-1]
        b, bidx = l[i]
        x = (a & b)
        for j in range(k):
            x ^= (1 << j)
        v = ((a ^ x) & (b ^ x))
        if v > ans:
            ans = v
            ai, bi, xi = aidx, bidx, x
    print(ai, bi, xi)