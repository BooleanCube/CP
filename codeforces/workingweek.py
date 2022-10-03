t=int(input())
for z in range(t):
    n = int(input())
    if n==6:print(0);continue
    a,b = 1,round((n-4)/3)
    c = n-3-a-b
    print(min(abs(a-b),abs(b-c),abs(c-a)))
