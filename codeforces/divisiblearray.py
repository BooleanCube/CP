t = int(input())
for _ in range(t):
    n = int(input())
    l = list(range(1, n+1))
    s = sum(l)
    if s%n == 0:
        print(*l)
    else:
        l[s%n-1] += s%n
        print(*l)
