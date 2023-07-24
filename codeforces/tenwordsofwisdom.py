t = int(input())

for _ in range(t):
    n = int(input())
    l = []
    for i in range(n):
        a,b = map(int, input().split())
        if a<=10:
            l.append((b, i+1))

    print(max(l)[1])
