t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = sorted([(val%k if val%k>0 else k, n-idx-1) for idx, val in enumerate(list(map(int, input().split())))], reverse=True)
    print(*[n-c[1] for c in l])
