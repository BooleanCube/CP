t=int(input())
for i in range(t):
    input()
    l = list(map(int,input().split()))
    a = 0
    b = True
    for j in l:
        a += j
        if a<0:
            b=False
            break
    b &= sum(l)==0
    print("Yes" if b else "No")
