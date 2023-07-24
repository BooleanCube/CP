t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    diff = 1e99
    for i in range(1, n):
        diff = min(diff, l[i]-l[i-1])
    print(max(0, diff//2+1))
