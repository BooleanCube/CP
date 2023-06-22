t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print(sum(l[-i-1]-l[i] for i in range(n//2)))
