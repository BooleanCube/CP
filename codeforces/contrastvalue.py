t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if len(set(l)) == 1:
        print(1)
        continue
    if n < 3:
        print(n)
        continue
    s = 0
    d = 1 if l[0]<=l[1]<=l[2] else 0
    for i in range(n-2):
        a,b,c = l[i],l[i+1],l[i+2]
        if a<=b<=c:
            if not d:
                s -= 1
            d = 1
            s += 1
        elif a>=b>=c:
            if d:
                s -= 1
            d = 0
            s += 1
    print(n-s)
