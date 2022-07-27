t=int(input())
for i in range(t):
    n=int(input())
    a=n/6
    b=n/4
    if a%1!=0 and b%1!=0:
        print(-1)
    elif a%1==0 and b%1!=0:
        print(int(a),int(a))
    elif a%1!=0 and b%1==0:
        print(int(b),int(b))
    else:
        print(int(a),int(b))

