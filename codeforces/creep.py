t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    r=""
    for i in range(min(a,b)):r+="10"
    if a>b:
        r+="0"*(a-b)
    elif b>a:
        r+="1"*(b-a)
    print(r)
